import fitz
import os
import numpy as np
import json
from paddleocr import PaddleOCR
from random import randint
from typing import List, Optional


def check_reptition(file_path:str)->np.bool_:
    """
    Check whether the file has been already processed by us
    We consider the following dimensions for determination:
    
    1. Format
    2. File Size
    3. file page numbers
    4. If file has text
    5. If it has text, its length in total in a random page
    6. If it has same text length, its string hash in a random page

    Result:

    True: We process this document since it's new

    False: We don't process this document because it's not pdf or it's already processed
    """
    if not(len(file_path)>3 and file_path[-4:]==".pdf"):
        return False
    recordsFileModified = {}
    logPath = "logs/modified_files.json"
    if not os.path.exists(logPath):
        file_initial = open("logs/modified_files.json", "w")
        file_initial.close()
    elif os.path.getsize(logPath)>0:
        with open(logPath, "r") as f:
            recordsFileModified = json.load(f)

    doc = fitz.open(file_path)
    metadata = doc.metadata
    if metadata["format"] in recordsFileModified:
        pageLength = len(doc)
        if pageLength in recordsFileModified[metadata["format"]]:
            fileSize = os.path.getsize(file_path)
            if fileSize in recordsFileModified[metadata["format"]][pageLength]:
                randNum = randint(0, pageLength)
                text = doc[randNum].get_text()
                textLength = len(text)
                textHash = hash(text)
                if textLength in recordsFileModified[metadata["format"]][pageLength][fileSize]:
                    if textLength in recordsFileModified[metadata["format"]][pageLength][fileSize][textLength]==textHash:
                        return False
    return True


def extractTextFromPdf(file_path:str, page_start:int = 0, page_end:int = 1, filename:str = "", saveRoute:str = ".", lang:str = "fr", show_log = False):
    doc = fitz.open(file_path)
    ocr = PaddleOCR(use_angle_cls=True, lang=lang ,page_num=len(doc) ,show_log = show_log)  # need to run only once to download and load model into memory
    result = ocr.ocr(file_path, cls=True)
    for i in range(page_start, page_end):
        page = doc[i]
        image_size = result[i][-1]
        for rectangle, text_area in result[i][:-1]:
            rectangle.sort()
            p_bl = rectangle[0]
            rectangle.sort(key = lambda x:x[1])
            p_bl[1] = rectangle[-1][1]
            pix = page.get_pixmap()
            long, height = pix.width, pix.height
            #print("check format:", p_bl, image_size)
            rl, rh = image_size[1], image_size[0]
            p_bl = [(p_bl[0]*long)/rl, (p_bl[1]*height)/rh]
            if text_area[1]>=0.7:
                text = text_area[0]
                ll = page.insert_text(point=p_bl, text = text, fontfile="fonts/french.ttf",color=(0, 0, 0), stroke_opacity=0, fill_opacity=0,)
    return doc

def saveFileToDst(doc, filePath:str):
    doc = doc[0]
    doc.save(filePath, garbage=3, deflate=True)
    """
    Save Record to Logs to avoid repetitive extraction of same file
    """
    recordsFileModified = {}
    if os.path.getsize("./logs/modified_files.json")>0:
        with open("./logs/modified_files.json", "r") as f:
            recordsFileModified = json.load(f)
    
    metadata = doc.metadata
    fileSize = os.path.getsize(filePath)
    randNum = randint(0, len(doc)-1)
    text = doc[randNum].get_text()
    textLength = len(text)
    textHash = hash(text)
    pageLength = len(doc)
    with open("logs/modified_files.json", "w") as f:
        if metadata["format"] in recordsFileModified:
            if pageLength in recordsFileModified[metadata["format"]]:
                if fileSize in recordsFileModified[metadata["format"]][pageLength]:
                    if textLength in recordsFileModified[metadata["format"]][pageLength][fileSize]:
                        if textHash not in recordsFileModified[metadata["format"]][pageLength][fileSize][textLength]:
                            recordsFileModified[metadata["format"]][pageLength][fileSize][textLength] = [textHash]
                    else:
                        recordsFileModified[metadata["format"]][pageLength][fileSize][textLength].append(textHash)
                else:
                    recordsFileModified[metadata["format"]][pageLength][fileSize] = {textLength:[textHash]}
            else:
                recordsFileModified[metadata["format"]][pageLength] = {fileSize:{textLength:[textHash]}}
        else:
            recordsFileModified[metadata["format"]] = {pageLength:{fileSize:{textLength:[textHash]}}}
        json.dump(recordsFileModified, f)
    return None