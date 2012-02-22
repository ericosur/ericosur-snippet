#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Project       FreeImagePy
# file name:    FreeImagePy.py
#
# $Id $
#
# DESCRIPTION
# FreeImage python bind
#
# Developer:
# Michele Petrazzo <michele.petrazzo@unipex.it>
#
# History : (see ChangeLog.txt for more info)
# creation: 08/2005 - Michele Petrazzo
#
# V1.3.0:
#           07/2006 - Michele Petrazzo
#
# V1.2.5:
#           04/2006 - Michele Petrazzo
# V1.2.4:
#           02/2006 - Michele Petrazzo
# V1.2:
#           01/2006 - Michele Petrazzo
#
# V1.1:     09/2005 - Lenard Lindstrom (Handle methods and tests)
#                     Michele Petrazzo
# 
# License:
#         GNU General Public License (GPL)
#         FreeImage Public License (FIPL)
#         For more info see LICENSE.txt
#
# Copyright (C) 2005  Unipex s.r.l.,  All Rights Reserved.
# Via Vittorio Veneto 83/A
# 33050 Gonars (UD) - Italy
# tel. +39 0432 931511 - fax +39 0432 931378
# www.unipex.it - michele.petrazzo@unipex.it
#

import ctypes as C
import os, os.path, tempfile, sys, time, StringIO
from warnings import warn

#Load the constants
from constants import *
from utils import *
from buffer import *
import library

from funct_list import FUNCTION_LIST

#FreeImage class list
_freeImgLst = list()

class freeimage(object):
    
    """ 
    FreeImage class wrapper
    
    The method with the first line uppercase are internal library methods
    the other one are internal method for help the user
        
    @author: Michele Petrazzo
    @author: Lenard Lindstrom (handle functions)
    """
    
    def __init__(self, libraryName=None):
        """
        Init method for the class
        
        @param libraryName: library path, otherwise I'll look for it into the
                            standard path
        @type libraryName: string
        """
        
        # Used for test
        self.__num = 0
        # Used for test
        
        self.initCalled = 0
        self.__lib = library.internlLibrary(libraryName)
        if self.__lib.getStatus()[0]:
            return 'Error: %s' % str(self.__lib.getStatus())
        
        global _freeImgLst
        _freeImgLst.append(self.__lib)

    # ------------------ #
    #  General funtions  #
    # ------------------ #
    
    def GetCopyrightMessage(self):
        """ Returns a string containing a standard copyright message you 
            can show in your program.
        """
        return self.__lib.GetCopyrightMessage()
    
    def GetVersion(self):
        """ Returns a string containing the current version of the DLL.
        """
        return self.__lib.GetVersion()
    
    def Initialise(self, loadPlugin = False):
        """ Initialises the library. When the loadPlugin 
        parameter is TRUE, FreeImage won t make use of external plugins.
        """
        return self.__lib.Initialise(loadPlugin)

    def DeInitialise(self):
        """ Deinitialises the library.
        """
        if sys.platform == 'win32': return True
        
        global _freeImgLst
        if self.__lib in _freeImgLst:
            _freeImgLst.remove(self.__lib)
        
        #See how many libraries are instanced and if need, call deinit
        if len(_freeImgLst) == 1:
            return self.__lib.DeInitialise()
        else:
            return 0
        return self.__lib.DeInitialise()
        
    def Allocate(self, widht, height, bpp, 
                redMask=False, greenMask=False, blueMask=False):
        """ If you want to create a new bitmap in memory from scratch, 
            without loading a pre-made bitmap from disc, you use this function.
        """
        return self.__lib.Allocate(widht, height, bpp, 
                    redMask, greenMask, blueMask)
    
    def AllocateT(self, type, width, height, bpp=8, red_mask=0, green_mask=0, 
            blue_mask=0):
        """
        """
        self.__ctrlColorUsed()
        return self.__lib.AllocateT(type, width, height, bpp, red_mask, 
                    green_mask, blue_mask)
    
    def Clone(self, bitmap):
        """ Makes an exact reproduction of an existing bitmap
        """
        self.__ctrlColorUsed()
        return self.__lib.Clone(bitmap)

    def Load(self, typ, fileName, flags=False):
        """ This function decodes a bitmap, allocates
            memory for it and then returns it as a FIBITMAP.
        """
        #Make unicode control
        if isinstance(fileName, unicode):
            if sys.platform == 'win32':
                return self.LoadU(typ, fileName, flags)
            else:
                fileName = C.c_char_p(fileName)
        
        return self.__lib.Load(typ, fileName, flags)

    def LoadU(self, typ, fileName, flags=False):
        """ Same of Load. UNICODE version. Work only on win32 systems
            @see: Load
        """
        if not sys.platform == 'win32':
            return self.Load(typ, fileName, flags)
            
        return self.__lib.LoadU(typ, fileName, flags)

    def LoadFromHandle(self, typ, io_p, handle, flags=False):
        """ This function is the handle version of Load.
        """
        return self.__lib.LoadFromHandle(typ, io_p, handle, flags)

    def Save(self, typ, bitmap, fileName, flags=False):
        """ This function saves a previously loaded FIBITMAP to a file.
        """
        #Make unicode control
        if isinstance(fileName, unicode):
            if sys.platform == 'win32':
                return self.SaveU(typ, bitmap, fileName, flags)
            else:
                fileName = C.c_char_p(fileName)
        
        return self.__lib.Save(typ, bitmap, fileName, flags)

    def SaveU(self, typ, bitmap, fileName, flags=False):
        """ Same of Save. UNICODE version. Work only on win32 systems.
            @see: Save
        """

        if not sys.platform == 'win32':
            return self.Save(typ, bitmap, fileName, flags)
        
        return self.__lib.SaveU(typ, bitmap, fileName, flags)

    def SaveToHandle(self, typ, bitmap, io, handle, flags=False):
        """ This function saves a previously loadaed FIBITMAP to a file handle.
        """
        return self.__lib.SaveToHandle(typ, bitmap, io, handle, flags)

    def Unload(self, bitmap):
        """ Deletes a previously loaded FIBITMAP from memory. 
            You always need to call this function once you are done 
            with a bitmap, or you will have a memory leak
        """
        return self.__lib.Unload(bitmap)

    # ------------------- #
    #  MultiPage methods  #
    # ------------------- #
    
    def OpenMultiBitmap(self, format, fileName, create=False, readOnly=False,
                        keepInMemory=True, flags=False):

        """ flags is to enable or disable a feature into a plugin
        """
        fileName = C.c_char_p(fileName)
        return self.__lib.OpenMultiBitmap(format, fileName, create, readOnly,
                        keepInMemory, flags)
        
    def GetPageCount(self, multiBitmap):
        """ Return how many pages are present into this bitmap
        """
        return self.__lib.GetPageCount(multiBitmap)
    
    def LockPage(self, multiBitmap, page):
        """ Lock and return a locked bitmap into a multipage bitmap

            @param multiBitmap: the multibitmap image
            @param page: the page to lock
            @type page: int
        """
        p = INT(page)
        return self.__lib.LockPage(multiBitmap, p)
    
    def UnlockPage(self, multiBitmap, bitmap, modified=False):
        """ UnLock a page into a multipage bitmap
            if modified, the engine update the bitmap with that passed
            
            @param multiBitmap: the multibitmap image
            @param bitmap: the bitmap to unlock
        """
        return self.__lib.UnlockPage(multiBitmap, bitmap, modified)
    
    def AppendPage(self, multiBitmap, data):
        """ Append data page to the bitmap's end

            @param multiBitmap: the multibitmap image
            @param data: the bitmap already loaded to append
        """
        return self.__lib.AppendPage(multiBitmap, data)

    def CloseMultiBitmap(self, multiBitmap, flags=False):
        """ Flags is to enable or disable a feature into a plugin
        """
        return self.__lib.CloseMultiBitmap(multiBitmap, flags)

    def DeletePage(self, multiBitmap, page):
        """ Deletes the page on the given position.

            @param multiBitmap: the multibitmap image
            @param page: the page to delete
            @type page: int
        """
        return self.__lib.DeletePage(multiBitmap, page)

    def MovePage(self, multiBitmap, target, source):
        """ Moves the source page to the position of the target page. 
            Returns TRUE on success, FALSE on failure.
            
            @type target: int
            @type source: int
        """
        return self.__lib.MovePage(multiBitmap, target, source)

    def GetLockedPageNumbers(self, multiBitmap, pages=None, count=None):
        """ Returns an array of page-numbers that are currently locked in memory.
        """
        if not (pages or count):
            nv = INT()
            self.__lib.GetLockedPageNumbers(multiBitmap, None, C.pointer(nv))
            if nv.value == 0: return []
            AR = INT * nv.value
            pages = AR(10)
            count = INT(nv.value)

        self.__lib.GetLockedPageNumbers(multiBitmap, C.byref(pages), C.byref(count))
        return [x for x in pages]

    def InsertPage(self, multiBitmap, page, data):
        """ Inserts a new page before the given position in the bitmap.
            
            @param multiBitmap: the multibitmap image
            @param page: the page to delete
            @type page: int
            @param data: the bitmap already loaded
        """
        return self.__lib.InsertPage(multiBitmap, page, data)


    # ----------------- #
    #  Plugin functions #
    # ----------------- #
    
    def FIFSupportsReading(self, fif):
        """ Returns TRUE if the plugin belonging to the given 
            FREE_IMAGE_FORMAT can be used to
            load bitmaps, FALSE otherwise.
        """
        return self.__lib.FIFSupportsReading(fif)
    
    def GetFIFFromFilename(self, fileName):
        """This function takes a filename or a file-extension and returns
        the plugin that can read/write files with that extension in
        the form of a FREE_IMAGE_FORMAT identifier.
        """
        #Make unicode control
        if isinstance(fileName, unicode):
            if sys.platform == 'win32':
                return self.GetFIFFromFilenameU(fileName)
            else:
                fileName = C.c_char_p(fileName)
        
        return self.__lib.GetFIFFromFilename(fileName)

    def GetFIFFromFilenameU(self, fileName):
        """Same of GetfiFFromFilename. 
            UNICODE version. Work only on win32 systems
            @see: GetfiFFromFilename
        """
        if not sys.platform == 'win32':
            return self.GetFIFFromFilename(fileName)
            
        return self.__lib.GetFIFFromFilenameU(fileName)
        
    
    def FIFSupportsExportBPP(self, fif, bpp):
        """ Returns TRUE if the plugin belonging to the given 
            FREE_IMAGE_FORMAT can save a bitmap in the desired bit depth
        """
        return self.__lib.FIFSupportsExportBPP(fif, bpp)

    def FIFSupportsExportType(self, fif, type):
        """ Returns TRUE if the plugin belonging to the given 
            FREE_IMAGE_FORMAT can save a bitmap in the desired data type,
        """
        return self.__lib.FIFSupportsExportType(bitmap, fif, type)

    def FIFSupportsICCProfiles(self, fif):
        """ Returns TRUE if the plugin belonging to the given 
            FREE_IMAGE_FORMAT can load or save an ICC profile,
        """
        return self.__lib.FIFSupportsICCProfiles(bitmap, fif)

    def FIFSupportsWriting(self, fif):
        """ Returns TRUE if the plugin belonging to the given FREE_IMAGE_FORMAT 
        can be used to save bitmaps
        """
        return self.__lib.FIFSupportsWriting(bitmap, fif)    

    def GetFIFCount(self):
        """ Retrieves the number of FREE_IMAGE_FORMAT identifiers being 
            currently registered.
        """
        return self.__lib.GetFIFCount()

    def GetFIFDescription(self, fif):
        """ Returns a descriptive string that describes the bitmap formats 
            the given plugin can read and/or write.
        """
        return self.__lib.GetFIFDescription(bitmap)

    def GetFIFExtensionList(self):
        """ Returns a comma-delimited file extension list describing
            the bitmap formats the given plugin can read and/or write.
        """
        return self.__lib.GetFIFExtensionList()

    def GetFIFFromFormat(self, format):
        """ Returns a FREE_IMAGE_FORMAT identifier from the format 
            string that was used to register the FIF.
        """
        return self.__lib.GetFIFFromFormat(format)

    def GetFIFFromMime(self, mime):
        """ Returns a FREE_IMAGE_FORMAT identifier from a MIME content type 
        string (MIME stands for Multipurpose Internet Mail Extension).
        """
        return self.__lib.GetFIFFromMime(mime)

    def GetFIFMimeType(self, fif):
        """ Given a FREE_IMAGE_FORMAT identifier, returns a MIME content type 
        string (MIME stands for Multipurpose Internet Mail Extension).
        """
        return self.__lib.GetFIFMimeType(fif)

    def GetFIFRegExpr(self, fif):
        """ Returns a comma-delimited file extension list describing 
            the bitmap formats the given plugin can read and/or write.
        """
        return self.__lib.GetFIFRegExpr(fif)
    
    def GetFormatFromFIF(self, fif):
        """ Returns the string that was used to register a plugin from the 
            system assigned FREE_IMAGE_FORMAT.
        """
        return self.__lib.GetFormatFromFIF(fif)

    def IsPluginEnabled(self, fif):
        """ Returns TRUE when the plugin is enabled, FALSE when the plugin is 
            disabled, -1 otherwise.
        """
        return self.__lib.IsPluginEnabled(fif)
    
    def RegisterExternalPlugin(self, path, format=0, description=0, extension=0, 
            regexpr = 0):
        """ Registers a new plugin to be used in FreeImage.
        """
        return self.__lib.RegisterExternalPlugin(path, format, description, 
                    extension, regexpr)

    def RegisterLocalPlugin(self, proc_address, format=0, description=0, extension=0, 
            regexpr = 0):
        """ Registers a new plugin to be used in FreeImage.
        """
        return self.__lib.RegisterLocalPlugin(proc_address, format, description, 
                    extension, regexpr)

    def SetPluginEnabled(self, fif, enabled):
        """ Enables or disables a plugin.
        """
        return self.__lib.SetPluginEnabled(fif, enabled)
    
    # ------------------- #
    #  Bitmap information #
    # ------------------- #

    def GetBackgroundColor(self, bitmap):
        """ Retrieves the file background color of an image.
        """
        self.__ctrlColorUsed()
        bkcolor = RGBQUAD()
        self.__lib.GetBackgroundColor(bitmap, C.pointer( bkcolor ))
        color = dict( [("red", bkcolor.rgbRed), ("green", bkcolor.rgbGreen), ("blue", bkcolor.rgbBlue)] )
        return color


    def GetFileType(self, fileName, size=False):
        """ Return the file type, like bmp, tiff, png
            This function return a value that are used in other functions
            that need the bitmap type
            Size it not used into the library
        """
        #Make unicode control
        if isinstance(fileName, unicode):
            if sys.platform == 'win32':
                return self.GetFileTypeU(fileName)
            else:
                fileName = C.c_char_p(fileName)
        
        return self.__lib.GetFileType(fileName, size)

    def GetFileTypeU(self, fileName, size=False):
        """ Unicode version of GetFileType
            @see: GetFileType
        """
        if not sys.platform == 'win32':
            return self.GetFileType(fileName)
        
        return self.__lib.GetFileTypeU(fileName, size)

    def GetFileTypeFromHandle(self, io_p, handle, flags=False):
        """ Uses the FreeImageIO structure to identify a bitmap type
        """
        return self.__lib.GetFileTypeFromHandle(io_p, handle, flags)

    def GetColorType(self, bitmap):
        """ Returm one of the FIC_* values
        """
        #self.__ctrlColorUsed()
        return self.__lib.GetColorType(bitmap)
    
    def GetImageType(self, bitmap):
        """ Return the image type
        """
        self.__ctrlColorUsed()
        return self.__lib.GetImageType(bitmap)

    def GetWidth(self, bitmap):
        """ Return the bitmap width
        """
        self.__ctrlColorUsed()
        return self.__lib.GetWidth(bitmap)

    def GetHeight(self, bitmap):
        """ Return the bitmap height
        """
        self.__ctrlColorUsed()
        return self.__lib.GetHeight(bitmap)
    
    def GetBPP(self, bitmap):
        """ Return the depth
        """
        return self.__lib.GetBPP(bitmap)
    
    def GetDotsPerMeterX(self, bitmap):
        """ Return the horrizontal resolution
        """
        self.__ctrlColorUsed()
        return self.__lib.GetDotsPerMeterX(bitmap)

    def GetDotsPerMeterY(self, bitmap):
        """ Return the vertical resolution
        """
        self.__ctrlColorUsed()
        return self.__lib.GetDotsPerMeterY(bitmap)
    
    def SetDotsPerMeterX(self, bitmap, res):
        """ Set the horrizontal resolution
        """
        self.__ctrlColorUsed()
        return self.__lib.SetDotsPerMeterX(bitmap, res)

    def SetDotsPerMeterY(self, bitmap, res):
        """ Set the vertical resolution
        """
        self.__ctrlColorUsed()
        return self.__lib.SetDotsPerMeterY(bitmap, res)
    
    def GetColorsUsed(self, bitmap):
        """ Return the number of color used
        """
        self.__ctrlColorUsed()
        return self.__lib.GetColorsUsed(bitmap)
    
    def GetPalette(self, bitmap):
        """ Return a pointer to a palette struct 
        """
        self.__ctrlColorUsed()
        return self.__lib.GetPalette(bitmap)

    def GetBlueMask(self, bitmap):
        """ Returns a bit pattern describing the blue color component of a 
            pixel in a FIBITMAP.
        """
        self.__ctrlColorUsed()
        return self.__lib.GetBlueMask(bitmap)

    def GetRedMask(self, bitmap):
        """ Like up
        """
        self.__ctrlColorUsed()
        return self.__lib.GetRedMask(bitmap)
    
    def GetGreenMask(self, bitmap):
        """ Like up
        """
        self.__ctrlColorUsed()
        return self.__lib.GetGreenMask(bitmap)

    def GetInfoHeader(self, bitmap):
        """ Returns a pointer to the BITMAPINFOHEADER of the DIB-element in
            a FIBITMAP.
        """
        self.__ctrlColorUsed()
        return self.__lib.GetInfoHeader(bitmap)

    def GetInfo(self, bitmap):
        """ Alias for GetInfoHeader
        """
        return self.GetInfoHeader(bitmap)
        
    def GetLine(self, bitmap):
        """ Returns the width of the bitmap in bytes.
            See also: FreeImage_GetPitch.
        """
        self.__ctrlColorUsed()
        return self.__lib.GetLine(bitmap)

    def GetPitch(self, bitmap):
        """ Returns the width of the bitmap in bytes, rounded to the next 
            32-bit boundary, also known as pitch or stride or scan width.
            
            @bug: If bitmap bpp aren't 24 or 32, this function may not return the
            right value.
        """
        self.__ctrlColorUsed()
        
        #TODO: help me for solve this?
        #Warn for a possible problem!
        if self.__lib.GetBPP(bitmap) not in (24, 32):
            msg = """
            This bitmap don't has 24 or 32 bpp.
            The value returned cannot be right.
            See the doc and if you can, help me to solve it"""
            warn(msg)
        
        return self.__lib.GetPitch(bitmap)
    
    def SetTransparencyTable(self, bitmap, table, count):
        """ Set the bitmap s transparency table.
        """
        self.__ctrlColorUsed()
        return self.__lib.SetTransparencyTable(bitmap, table, count)

    def IsTransparent(self, bitmap):
        """ Returns TRUE when the transparency table is enabled
        """
        self.__ctrlColorUsed()
        return self.__lib.IsTransparent(bitmap)

    def SetTransparent(self, bitmap, enabled):
        """ Tells FreeImage if it should make use of the transparency table 
        that may accompany a bitmap
        """
        self.__ctrlColorUsed()
        return self.__lib.SetTransparent(bitmap, enabled)
    
    def SetBackgroundColor(self, bitmap, color):
        """ Set the file background color of an image.
        """
        self.__ctrlColorUsed()
        
        bkcolor = RGBQUAD()
        bkcolor.rgbRed = color["red"]
        bkcolor.rgbGreen = color["green"]
        bkcolor.rgbBlue = color["blue"]
        
        return self.__lib.SetBackgroundColor(bitmap, C.pointer( bkcolor) )
    
    def GetTransparencyCount(self, bitmap):
        """ Returns the number of transparent colors in a palletised bitmap
        """
        self.__ctrlColorUsed()
        return self.__lib.GetTransparencyCount(bitmap)

    def GetTransparencyTable(self, bitmap):
        """ Returns a pointer to the bitmap s transparency table.
        """
        self.__ctrlColorUsed()
        return self.__lib.GetTransparencyTable(bitmap)

    def HasBackgroundColor(self, bitmap):
        """ Returns TRUE when the image has a file background color
        """
        self.__ctrlColorUsed()
        return self.__lib.HasBackgroundColor(bitmap)
        
    # ----------------------- #
    #   Pixel access methods  #
    # ----------------------- #

    def GetPixelIndex(self, bitmap, x=0, y=0):
        """ Return the pixel index for the bitmap,
            default return the first at left top
        """
        self.__ctrlColorUsed()
        value = BYTE()
        xP = C.c_uint(x)
        yP = C.c_uint(y)
        self.__lib.GetPixelIndex( bitmap, xP, yP, C.pointer(value))
        return value.value
    
    def GetBits(self, bitmap):
        """ 
            Returns a pointer to the data-bits of the bitmap.
            
            @param bitmap: bitmap
            @type bitmap: int
        """
        return self.__lib.GetBits(bitmap)
    
    def GetPixelColor(self, bitmap, x, y, value=None):
        """ Get the pixel color of a 16-, 24- or 32-bit image at position 
        (x, y), including range check (slow access).
        """
        if not value: value = C.POINTER(RGBQUAD)
        self.__ctrlColorUsed()
        return self.__lib.GetPixelColor(bitmap, x, y, value), value

    def GetScanLine(self, bitmap, scanline):
        """ Returns a pointer to the start of the given scanline in 
            the bitmap s data-bits.
        """
        self.__ctrlColorUsed()
        return self.__lib.GetScanLine(bitmap, scanline)

    def SetPixelColor(self, bitmap, x, y, value=None):
        """ Set the pixel color of a 16-, 24- or 32-bit image at position 
            (x, y), including range check (slow access).
        """
        if not value: value = C.POINTER(RGBQUAD)
        self.__ctrlColorUsed()
        return self.__lib.SetPixelColor(bitmap, x, y, value), value

    def SetPixelIndex(self, bitmap, x, y, value=None):
        """ Set the pixel index of a palettized image at position (x, y), 
            including range check (slow access).
        """
        if not value: value = C.POINTER(RGBQUAD)
        self.__ctrlColorUsed()
        return self.__lib.SetPixelIndex(bitmap, x, y, value), value

    
    # -------------------------------------- #
    #   Conversion / Trasformation methods   #
    # -------------------------------------- #
    
    def Rescale(self, bitmap, dstWidth, dstHeight, filter=FILTER_BSPLINE, close=0):
        """ Return the bitmap rescaled with the parameter passed
        """
        self.__ctrlColorUsed()
        new_bitmap = self.__lib.Rescale(bitmap, int(dstWidth), int(dstHeight), filter)
        self.__closeIf(bitmap, close)
        return new_bitmap
    
    def MakeThumbnail(self, bitmap, max_pixel_size, convert=True, close=0):
        """
        """
        self.__ctrlColorUsed()
        new_bitmap = self.__lib.MakeThumbnail(bitmap, max_pixel_size, convert)
        self.__closeIf(bitmap, close)
        return new_bitmap
        
    def Dither(self, bitmap, matrix=FID_FS):
        """ Transfom (out will be 1 bit per pixel) and return a copy of the bitmap
        """
        self.__ctrlColorUsed()
        return self.__lib.Dither(bitmap, matrix)
    
    def RotateClassic(self, bitmap, angle, close=0):
        """ Rotate the bitmap and return a new bitmap
        """
        self.__ctrlColorUsed()
        new_bitmap = self.__lib.RotateClassic(bitmap, C.c_double(angle))
        self.__closeIf(bitmap, close)
        return new_bitmap

    def RotateEx(self, bitmap, angle, x_shift, y_shift, x_origin, y_origin, 
                use_mask):
        """ This function performs a rotation and / or translation of an 8-bit 
            greyscale, 24- or 32-bit image, using a 3rd order (cubic) B-Spline.
        """
        self.__ctrlColorUsed()
        return self.__lib.RotateEx(bitmap,  angle, x_shift, y_shift, x_origin, 
                y_origin, use_mask)
    
    def ConvertTo4Bits(self, bitmap, close=0):
        """ Convert the bitmap to 4 bits depth
            and optionally close it
        """
        self.__ctrlColorUsed()
        new_bitmap = self.__lib.ConvertTo4Bits(bitmap)
        self.__closeIf(bitmap, close)
        return new_bitmap
    
    def ConvertTo8Bits(self, bitmap, close=0):
        """ Convert the bitmap to 8 bits depth
            and optionally close it
        """
        self.__ctrlColorUsed()
        new_bitmap = self.__lib.ConvertTo8Bits(bitmap)
        self.__closeIf(bitmap, close)
        return new_bitmap

    def ConvertToGreyscale(self, bitmap, close=0):
        """ Converts a bitmap to a 8-bit greyscale image with a linear ramp
            and optionally close it
        """
        self.__ctrlColorUsed()
        new_bitmap = self.__lib.ConvertToGreyscale(bitmap)
        self.__closeIf(bitmap, close)
        return new_bitmap
    
    
    def ConvertTo16Bits555(self, bitmap, close=0):
        """ Convert the bitmap to 16/555 bits depth
            and optionally close it
        """
        self.__ctrlColorUsed()
        new_bitmap = self.__lib.ConvertTo16Bits555(bitmap)
        self.__closeIf(bitmap, close)
        return new_bitmap

    def ConvertTo16Bits565(self, bitmap, close=0):
        """ Convert the bitmap to 16/565 bits depth
            and optionally close it
        """
        self.__ctrlColorUsed()
        new_bitmap = self.__lib.ConvertTo16Bits565(bitmap)
        self.__closeIf(bitmap, close)
        return new_bitmap

    def ConvertTo32Bits(self, bitmap, close=0):
        """ Convert the bitmap to 64 bits depth
            and optionally close it
        """
        self.__ctrlColorUsed()
        new_bitmap = self.__lib.ConvertTo32Bits(bitmap)
        self.__closeIf(bitmap, close)
        return new_bitmap
    
    def ConvertToStandardType(self, bitmap, scale_linear = 1, close=0):
        """ Convert the passed image to a standard type
        """
        self.__ctrlColorUsed()
        new_bitmap = self.__lib.ConvertToStandardType(bitmap, scale_linear)
        self.__closeIf(bitmap, close)
        return new_bitmap
    
    def ColorQuantize(self, bitmap, quantize = FIQ_WUQUANT):
        """ Quantizes a high-color 24-bit bitmap to an 8-bit
            palette color bitmap. The quantize parameter
            specifies the color reduction algorithm to be used:
        """
        self.__ctrlColorUsed()
        return self.__lib.ColorQuantize(bitmap, quantize)

    def ColorQuantizeEx(self, bitmap, quantize = FIQ_WUQUANT, PaletteSize = 256,
                        ReserveSize = 0, ReservePalette = None):
        """ FreeImage_ColorQuantizeEx is an extension to the 
        FreeImage_ColorQuantize function that provides additional options
        """
        self.__ctrlColorUsed()
        return self.__lib.ColorQuantizeEx(bitmap, quantize, PaletteSize, \
                        ReserveSize, ReservePalette)

    def ConvertFromRawBits(self, bits, width, height, pitch, bpp, red_mask, 
                            green_mask, blue_mask, topdown = False):
        """ Converts a raw bitmap somewhere in memory to a FIBITMAP.
        """
        self.__ctrlColorUsed()
        return self.__lib.ConvertFromRawBits(bits, width, height, pitch, bpp, 
                            red_mask, green_mask, blue_mask, topdown)
                            
    def ConvertTo24Bits(self, bitmap, close=0):
        """
        """
        self.__ctrlColorUsed()
        new_bitmap = self.__lib.ConvertTo24Bits(bitmap)
        self.__closeIf(bitmap, close)
        return new_bitmap

    def ConvertToRawBits(self, bits, bitmap, pitch, bpp, red_mask, green_mask, 
            blue_mask, topdown = False):
        """ Converts a FIBITMAP to a raw piece of memory.
        """
        self.__ctrlColorUsed()
        return self.__lib.ConvertToRawBits(bits, bitmap, pitch, bpp, red_mask, 
                            green_mask, blue_mask, topdown)

    def ConvertToRGBF(self, bitmap):
        """ Converts a 24- or 32-bit RGB(A) standard image or a 48-bit 
            RGB image to a FIT_RGBF type image.
        """
        self.__ctrlColorUsed()
        return self.__lib.ConvertToRGBF(bitmap)

    def ConvertToType(self, bitmap, dst_type, scale_linear = True):
        """ Converts an image of any type to type dst_type.
        """
        self.__ctrlColorUsed()
        return self.__lib.ConvertToType(bitmap, dst_type, scale_linear )
    
    def Threshold(self, bitmap, T):
        """ Converts a bitmap to 1-bit monochrome bitmap using a 
            threshold T between [0..255].
        """
        self.__ctrlColorUsed()
        return self.__lib.Threshold(bitmap, T)
    
    def GetDIBSize(self, bitmap):
        """ Returns the size of the DIB-element of a FIBITMAP in memory
        """
        self.__ctrlColorUsed()
        return self.__lib.GetDIBSize(bitmap)
    
    
    # ---------------------------- #
    #  Color manipulation methods  #
    # ---------------------------- #

    def Invert(self, bitmap):
        """ Inverts each pixel data
        """
        self.__ctrlColorUsed()
        return self.__lib.Invert(bitmap)
    
    def AdjustBrightness(self, bitmap, percentage):
        """Adjusts the brightness of a 8-, 24- or 32-bit image by a 
            certain amount. 
        """
        self.__ctrlColorUsed()
        return self.__lib.AdjustContrast(bitmap, C.c_double(percentage) )

    def AdjustContrast(self, bitmap, percentage):
        """ Like up
        """
        self.__ctrlColorUsed()
        return self.__lib.AdjustContrast(bitmap, C.c_double(percentage))

    def AdjustCurve(self, bitmap, LUT, channel):
        """ Perfoms an histogram transformation on a 8-, 24- or 32-bit 
        image according to the values of a lookup table (LUT).
        """
        self.__ctrlColorUsed()
        return self.__lib.AdjustCurve(bitmap, LUT, channel)

    def AdjustGamma(self, bitmap, gamma):
        """ Performs gamma correction on a 8-, 24- or 32-bit image.
        """
        self.__ctrlColorUsed()
        return self.__lib.AdjustGamma(bitmap, C.c_double(gamma))

    def GetHistogram(self, bitmap, histo, channel):
        """ Computes the image histogram.
        """
        self.__ctrlColorUsed()
        return self.__lib.GetHistogram(bitmap, histo, channel)
    
    # ---------------------------- #
    #  Channel processing methods  #
    # ---------------------------- #

    def GetChannel(self, bitmap, channel):
        """ Retrieves the red, green, blue or alpha channel of a 24- or 32-bit 
            image.
        """
        self.__ctrlColorUsed()
        return self.__lib.GetChannel(bitmap, channel)

    def SetChannel(self, bitmap, bitmap8, channel):
        """ Insert a 8-bit dib into a 24- or 32-bit image. dib8 and dib must 
            have the same width and height.
        """
        self.__ctrlColorUsed()
        return self.__lib.SetChannel(bitmap, bitmap8, channel)

    def GetComplexChannel(self, bitmap, channel):
        """ Retrieves the real part, imaginary part, magnitude or phase of a 
        complex image (image whose type is FIT_COMPLEX).
        """
        self.__ctrlColorUsed()
        return self.__lib.GetComplexChannel(bitmap, channel)
    
    def SetComplexChannel(self, bitmap, channel):
        """ Set the real or imaginary part of a complex image (image whose 
            type is FIT_COMPLEX).
        """
        self.__ctrlColorUsed()
        return self.__lib.SetComplexChannel(bitmap, channel)

    # ----------------------------------#
    # Copy / Paste / Composite routines #
    # ----------------------------------#

    def Copy(self, bitmap, left, top, right, bottom):
        """ Copy a sub part of the current dib image.
        """
        return self.__lib.Copy(bitmap, left, top, right, bottom)

    def Paste(self, bitmapTo, bitmap, left, top, alpha):
        """ Alpha blend or combine a sub part image with the current dib image.
            alpha : alpha blend factor. The source and destination images are alpha blended if
            alpha=0..255. If alpha > 255, then the source image is combined to the destination image.
        """
        self.__ctrlColorUsed()
        return self.__lib.Paste(bitmapTo, bitmap, left, top, alpha)
        
    # ---------------------------- #
    #   Tags and metadata methods  #
    # ---------------------------- #
    
    def GetTagValue(self, tag):
        """ Return the tag value
        """
        tt = self.GetTagType(tag)
        self.__lib.GetTagValue.restype = FIDT__LIST[tt]
        return self.__lib.GetTagValue(tag)
    
    def GetTagCount(self, tag):
        """ Returns the number of components in the tag (in tag type units).
        """
        return self.__lib.GetTagCount(tag)
    
    def GetTagID(self, tag):
        """ Returns the tag field name (unique inside a metadata model).
        """
        return self.__lib.GetTagID(tag)
    
    def GetTagType(self, tagId):
        """ Return the datatype
        """
        return self.__lib.GetTagType(tagId)
    
    def GetMetadata(self, mdModel, bitmap, key):
        """ Return metadata
        """
        tagName = VOID()
        self.__lib.GetMetadata(mdModel, bitmap, key, C.addressof(tagName))
        return tagName
    
    def GetMetadataCount(self, model, bitmap):
        """ Returns the number of components in the tag
        """
        return self.__lib.GetMetadataCount(model, bitmap)
    
    def FindFirstMetadata(self, model, dib, tag):
        """
        """
        if isinstance(tag, VOID):
            tag = C.addressof(tag)
        return self.__lib.FindFirstMetadata(model, dib, tag)
        
    def FindNextMetadata(self, handle, tag):
        """
        """
        if isinstance(tag, VOID):
            tag = C.addressof(tag)
        return self.__lib.FindNextMetadata(handle, tag)
    
    def FindCloseMetadata(self, handle):
        """
        """
        return self.__lib.FindCloseMetadata(handle)
        
    def GetTagDescription(self, tag):
        """ Returns the tag description if available, returns NULL otherwise.
        """
        if isinstance(tag, VOID):
            tag = C.addressof(tag)
        
        return self.__lib.GetTagDescription(tag)

    def TagToString(self, model, tag, make = None):
        """ Converts a FreeImage tag structure to a string that represents the 
            interpreted tag value.
        """
        return self.__lib.TagToString(model, tag, make)
    
    def GetTagKey(self, tag):
        """
        """
        return self.__lib.GetTagKey(tag)
        
        
    # ------------------------ #
    #   Help/internal methods  #
    # ------------------------ #

    def IsLittleEndian(self):
        """ This function returns TRUE if the platform running 
            FreeImage uses the Little Endian convention
        """
        return self.__lib.IsLittleEndian()


    def convertToMultiPage(self, filesIn, fileOut,
                            outFormat=-1, outBpp=-1,
                            sameSize=False,  sameType=False,
                            keepSizeFrom=0, keepTypeFrom=0,
                            flags=False, convertToFax=0,
                            deleteOld=0):
        
        """ Function for create the fileOut bitmap with fileIn list
            and optionally resize and convert the format of the bitmaps
            If you pass me format, I keep that like output format
            
            filesIn can be a list or tuple with (fileName, type) or only
            the filesNames, so I *try* to get the type
            
            deleteOld is used to tell me to delete the old files
        """
        
        #Try if we can read/write access to the output dir
        outDir = os.path.abspath( os.path.split(fileOut)[0] )
        try:
            file = tempfile.TemporaryFile(dir=outDir)
            time.sleep(0.1)
            file.close()
        except OSError:
            return 5, 'Error: cannot have read/write access to %s' % outDir

        #Delete the old file
        if os.path.exists(fileOut):
            try: os.remove(fileOut)
            except OSError: return 4, 'Error: cannot delete file %s' % fileOut
        
        #If convert to fax, I already know the type and the Bpp
        if convertToFax:
            outFormat = FIF_TIFF
            flags=TIFF_CCITTFAX4
            outBpp=1

        #Find the type
        elif outFormat == -1 and sameType:

            #Get the format
            outFormat = self.genericFileDeducer(filesIn[keepTypeFrom])

            #Get the format
            bmpForBpp = self.genericLoader(filesIn[keepTypeFrom])
            
            if not bmpForBpp:
                return 1, 'Error on type on outFormat'
            
            #Get the depth
            outBpp = self.GetBPP(bmpForBpp)
            
            self.Unload(bmpForBpp)
            
        elif outFormat == -1 and not sameType:
            FIF, ext, flag, fileOut = getParametersFromExt(fileOut)
            if FIF in (None, -1):
                return 1, 'Error: Specify a format, please'
            outFormat = FIF
            flags = flag
        
        #Find the size
        if sameSize and not convertToFax:
            bmpForType = self.genericLoader(filesIn[keepSizeFrom])
            if not bmpForType:
                return 1, 'Error: no type on sameSize'
            
            outW, outH = self.getSize(bmpForType)
            self.Unload(bmpForType)
        
        #The output bitmap
        outBmp = self.OpenMultiBitmap(outFormat, fileOut, True, flags=flags)
        if not outBmp:
            return 2, 'Error: I cannot open the multibitmap for write. Filename: %s , Format: %s, flags: %s' % \
                        ( fileOut, outFormat, flags)
        
        multiPageSplit = list()
        for ismultipage in filesIn:
            multiPageSplit += self.convertToSinglePages(ismultipage, FIF_PNG, 
                                '.png') #, returnOpenBitmap=1)
        
        for num, bmp in enumerate(multiPageSplit):
            
            #Control the types of passed paramenter
            if type(bmp) in ( list(), tuple() ):
                bmpFileName, bmpType = bmp
            else:
                bmpFileName = bmp
                bmpType = self.genericFileDeducer(bmpFileName)
                if bmpType == FIF_UNKNOWN:
                    return 1, 'Error: no find type on open %s' % bmpFileName
            
            #Load the bitmap
            bmpWork = self.Load(bmpType, bmpFileName)

            if not bmpWork:
                return 2, 'Error: I cannot open the bitmap %s' % bmpFileName

            #Size control
            if convertToFax: 
                bmpWork = self.convertToA4Fax(bmpWork)
            elif sameSize and num != keepSizeFrom:
                bmpWork = self.Rescale(bmpWork, outW, outH, close=1)
            
            # Type/depth control
            if sameType and num != keepTypeFrom and not convertToFax:
                bmpWork = self.setBppFromBpp(outBpp, bmpWork)
            
            self.AppendPage(outBmp, bmpWork)
            self.Unload(bmpWork)
            if deleteOld:
                try: 
                    if os.path.exists(bmpFileName): os.remove(bmpFileName)
                except OSError: pass
        
        self.CloseMultiBitmap(outBmp, flags)
        
        # Delete if it is request. I delete only the files that are created 
        # when I split the multipage bitmap that come-in
        for page in multiPageSplit:
            if page in filesIn: continue
            try: os.remove(page)
            except OSError: pass
        
        return 0, 'All ok!! File saved on %s' % fileOut

    def convertToA4Fax(self, bitmap):
        """ Convert the passed image to 1728 x 2210 pixel
            (206 x 196) DPI that is need when work with fax
        """

        W, H = self.getDotDPI(bitmap)
        X, Y = self.__getSize(bitmap) 

        #Control if the current file has the right resolution and size
        if not ( (W == 204 and H == 196) and (Y > X)):
            #Convert to 4 bits
            bitmap = self.setBppFromBpp(8, bitmap)
            bitmap = self.Rescale(bitmap, 1728, 2210, close=1)
        
        bitmap = self.ConvertToStandardType(bitmap, close=1)
        
        #Convert to 4 bits
        #self.Save(FIF_TIFF, bitmap, '/tmp/aaaaa_bef1%s.tif'% self.__num)
        bitmap = self.setBppFromBpp(1, bitmap)
        
        #self.Save(FIF_TIFF, bitmap, '/tmp/aaaaa_aft%s.tif'% self.__num)
        self.__convertToMinIsWhite(bitmap)
        
        self.setDotDPI(bitmap, (204, 196))
        
        #self.Save(FIF_TIFF, bitmap, './aaaaa_aft_2_%s.tif'% self.__num)
        self.__num+=1
        return bitmap

    def convertToMinIsWhite(self, bitmap):
        """ Invert the bitmap colors and the palette
            from minIsBlack to minIsWhite
        """
        self.__convertToMinIsWhite(bitmap)
    
    def convertPaletteToMinIsWhite(self, bitmap):
        """ Convert only the bitmap palette to minswhite
        """
        self.__convertToMinIsWhite(bitmap, False)
        
    def convertToSinglePages(self, multiPageName, outputFormat, outputExt, 
                        outputName=None, flags=None, bitmapType=-1, 
                        returnOpenBitmap=0, outputDir=None, outputDepth=-1):
        """ Return the multiPage splitted into single pages
            The returned name are "outputNameXXX.outputExt"
            Where XXX is a progressive number, started from 0
            If outputName isn't set, I create a new one name with tempfile
            
            If returnOpenBitmap is set, I return the opened bitmaps, 
            loaded into FITBITMAP structures
        """
        
        #Create the output file names if not present and delete it
        if not (outputName or returnOpenBitmap):
            if outputDir: fd, outputName = tempfile.mkstemp(dir=outputDir)
            else: fd, outputName = tempfile.mkstemp()
            f = os.fdopen(fd, 'w').close()
            try: os.remove(outputName)
            except OSError: pass
            
        if bitmapType == -1:
            bitmapType = self.genericFileDeducer(multiPageName)
        
        #Control if I'm a multibitmap
        ret_val, pageNum = self.isMultiPage(multiPageName, bitmapType)
        if ret_val: pageNum = 1
        
        if ret_val or (pageNum == 1 and outputFormat == bitmapType):
            if returnOpenBitmap:
                return [self.genericLoader(multiPageName),]
            else:
                return [multiPageName,]
        
        #Open multibitmap
        bitmapMulti = self.OpenMultiBitmap(bitmapType, multiPageName, False)
        if not bitmapMulti:
            return 2, 'This image is not a multiImage'
        fileNameList = list()
        
        #Iternate over the multipage bitmap
        for num in xrange( self.GetPageCount(bitmapMulti) ):
            
            bmpPage = self.LockPage(bitmapMulti, num)
            
            newBmp = None
            if outputDepth != -1:
                newBmp = self.setBppFromBpp(outputDepth, bmpPage, close=0)
            
            #If I have to return a loaded bitmap, clone it
            if returnOpenBitmap:
                if newBmp:  newBitmap = self.Clone(newBmp) 
                else:       newBitmap = self.Clone(bmpPage)
                fileNameList.append(newBitmap)
            
            #else, save it to a new file
            else:
                outputName = os.path.splitext(outputName)[0]
                fileNameOut = '%s%s%s' % (outputName, num, outputExt)
                if newBmp:
                    valRetSave = self.Save(outputFormat, newBmp, fileNameOut, flags)
                else:
                    valRetSave = self.Save(outputFormat, bmpPage, fileNameOut, flags)
                if not valRetSave: return 'Error: problems on save: %s' % fileNameOut
                fileNameList.append(fileNameOut)
            
            self.UnlockPage(bitmapMulti, bmpPage)
            if newBmp: self.Unload(newBmp)
            
        #Close and return the list
        self.CloseMultiBitmap(bitmapMulti)
        
        return  fileNameList
    
    def setBppFromBitmap(self, bitmapFrom, bitmapTo, close=1):
        """ Change the bitmapTo depth to the bitmapFrom depth
            If closeTo if true, if close I return the new bitmap and
            the close the oldBitmap one
        """
        depthF = self.GetBPP(bitmapFrom)
        return self.setBppFromBpp(depthF, bitmapFrom, close)
        
    
    def setBppFromBpp(self, BppFrom, bitmapTo, close=1):
        """ Change the bitmapTo depth to the bitmapFrom depth
            If closeTo if true, if close I return the new bitmap and
            the close the oldBitmap one
        """
        oldDpi = self.getDotDPI(bitmapTo)
        #If the bitmap has alreasy the right depth, return
        if self.GetBPP(bitmapTo) == BppFrom: 
            #print "setBppFromBpp already the right depth"
            return bitmapTo
        
        if BppFrom == 1:
            action = self.Dither
        elif BppFrom == 4:
            action = self.ConvertTo4Bits
        elif BppFrom == 8:
            action = self.ConvertTo8Bits
        elif BppFrom == 16:
            action = self.ConvertTo16Bits555
        elif BppFrom == 24:
            action = self.ConvertTo24Bits
        elif BppFrom == 32:
            action = self.ConvertTo32Bits
        else:
            self.__closeIf(bitmapTo, close)
            #I don't know how to convert the bitmap
            return 0
        
        new_bitmapTo = action(bitmapTo)
        self.__closeIf(bitmapTo, close)
        self.setDotDPI(new_bitmapTo, oldDpi)
        return new_bitmapTo
    
    def getSize(self, bitmap):
        """ Help method. Return a tuple with (widht, height)
        """
        return self.__getSize(bitmap)
    
    def getDotDPI(self, bitmap):
        """ Return the bitmap DPIs
        """
        W = int( round(self.GetDotsPerMeterX(bitmap) / 39.37) )
        H = int( round(self.GetDotsPerMeterY(bitmap) / 39.37 ) )
        return W, H

    def setDotDPI(self, bitmap, res):
        """ Return the bitmap DPIs
        """
        W, H = res
        return self.SetDotsPerMeterX(bitmap, int( round( W * 39.37)) ), \
               self.SetDotsPerMeterY(bitmap, int( round( H * 39.37)) )

    def openMulti(self, fileName, fileType=None):
        """ Simple mthod for open multibitmap page
        """
        if not fileType:
            fileType = self.genericFileDeducer(fileName)

        if fileType == FIF_UNKNOWN:
            return 1, 'Image type error'
        
        return self.OpenMultiBitmap(fileType, fileName, False)
        
    def isMultiPage(self, fileName, fileType=False):
        """ Return if the fileName passed is a multipage file
            the number of page is returned
        """
        if not fileType:
            fileType = self.genericFileDeducer(fileName)
        
        #If the bitmap hasn't the right type, ...
        if fileType == FIF_UNKNOWN:
            return 1, 'Image type error'
        elif fileType not in FIF_MUTLIPAGE:
            return 2, "Image is not a multipage type"
        
        bitmapMulti = self.OpenMultiBitmap(fileType, fileName, False)
        if not bitmapMulti:
            return 3, 'Cannot open image'
        
        pageN = self.GetPageCount(bitmapMulti)
        self.CloseMultiBitmap(bitmapMulti)
        return 0, pageN

    def loadFromFile(self, f, fif=None, flag=0):
        """ Load an image from an open python file object.
        """
        fileIO = FileIO(self, f)
        if fif is None: 
            fif = fileIO.getType()
        return fileIO.load(fif, flag)
    
    def saveToFile(self, fif, bitmap, f, flag=0):
        """ Save an image from an open python file object.
        """
        return FileIO(self, f).save(fif, bitmap, flag)

    def loadFromBuffer(self, buffer, fif=None, flag=0):
        """ Load an image from a buffer
        """
        StrIO = StringIO.StringIO(buffer)
        dib = self.loadFromFile(StrIO, fif, flag)
        StrIO.close()
        return dib
    
    def getBuffer(self, bitmap, close=0, topdown=False):
        """ Return the bitmap's buffer
        
            @param bitmap: bitmap
            @type bitmap: int
            @param close: if true, I'll close the bitmap
            @type close: int
            @param topdown: store the bitmap top-left pixel first when it is True 
                            or bottom-left pixel first when it is False.
            @type topdown: int
        """

        width, height = self.__getSize(bitmap)
        scan_width = self.GetPitch(bitmap)
        bpp = self.GetBPP(bitmap)
        
        # Allocate a raw buffer
        bits = C.create_string_buffer("\x00" * height * scan_width)

        self.ConvertToRawBits(C.byref(bits), bitmap, scan_width, bpp,
            FI_RGBA_RED_MASK, FI_RGBA_GREEN_MASK, FI_RGBA_BLUE_MASK, topdown)
        
        return bits.raw

    def genericLoader(self, fileName, flag=0):
        """ Check the file signature and deduce its format
            (the second argument is currently not used by FreeImage)
            return the bitmap loaded

            --- Thanks to the C++ code found on FreeImage examples
        """

        fif = self.genericFileDeducer(fileName)

        #If a type is found, return the loaded image
        if (fif != FIF_UNKNOWN) and self.FIFSupportsReading(fif):
            dib = self.Load(fif, fileName, flag);
            return dib
        #else return none
        return None

    def genericFileDeducer(self, fileName):
        """ Check the file signature and deduce its format
            (the second argument is currently not used by FreeImage)
            return the type

            --- Thanks to the C++ code found on FreeImage examples
        """
        fileName = C.c_char_p(fileName)
        fif = FIF_UNKNOWN
        try:
            fif = self.GetFileType(fileName)
            #I don't found any time
            if fif == FIF_UNKNOWN:
                fif = self.GetFIFFromFilename(fileName)
            return fif
        except:
            return fif

    def loadAndSave(self, fileNameLoad, dirNameSave, typeSave, fileLoadType=None):
        """ Load the passed filename and save it with the type
            If dirNameSave is a directory, I create a new filename with tempfile,
            else I save the new bitmap with that file name
            For typeSave argoument, if you can pass me a value (string) present into
            extToType dictionary, I see the type, flags and extension from there,
            else, pass me a list/tuple with this three values
        """
        
        if typeSave in extToType.keys():
            typeForSave, flagsForSave, extForSave = extToType[typeSave]
        else:
            typeForSave, flagsForSave, extForSave = typeSave
        
        if not fileLoadType:
            bitmap = self.genericLoader(fileNameLoad, flagsForSave)
        else:
            bitmap = self.Load(fileLoadType, fileNameLoad, flagsForSave)
        
        if not bitmap:
            return 'Error, cannot open %s' % fileNameLoad
        
        if os.path.isdir(dirNameSave):
            fileNameSave = tempfile.mkstemp(dir=dirNameSave, 
                            suffix=extForSave)[1]
        else:
            dirName, prefixName = os.path.split(dirNameSave)
            if prefixName.find(".") != -1:
                prefixName = os.path.splitext(prefixName)[0]
            fileNameSave = tempfile.mkstemp(dir=dirName,  prefix = prefixName,
                            suffix=extForSave)[1]
            
        #control the type
        if typeForSave == FIF_TIFF and flagsForSave in (TIFF_CCITTFAX3, TIFF_CCITTFAX4):
            new_bmp = self.setBppFromBpp(1, bitmap)
            bitmap = new_bmp
       
        self.Save(typeForSave, bitmap, fileNameSave, flagsForSave)
        return fileNameSave
    
    def getStatus(self):
        """ Return the library status 
        """
        return self.__lib.getStatus()

    def getTagValue(self, bitmap, model, keyName):
        """ Return the value of the key passed
        
            @param bitmap: A loaded bitmap
            @type bitmap: int (void)
            @param model: Model code
            @type model: FREE_IMAGE_MDMODEL (int)
            @param keyName: The key name
            @type keyName: string
        """
        
        tagName = self.GetMetadata(model, bitmap, keyName)
        return self.GetTagValue(tagName)
        
    
    def GetLibrary(self):
        """ Return the current library isntance. Use with careful
        """
        return self.__lib
    
    # ---------------- #
    #  Private methods #
    # ---------------- #
    
    def __convertToMinIsWhite(self, bitmap, invert=True):
        """ Internal method for convert to min is white
        """
        if not self.GetColorType(bitmap) == FIC_MINISBLACK: return

        if invert: self.Invert(bitmap)
        pointer = self.GetPalette(bitmap)
        
        for i in range(self.GetColorsUsed(bitmap)):
            cont = pointer[i]
            cont.rgbRed	  = 255 - cont.rgbRed
            cont.rgbGreen = 255 - cont.rgbGreen
            cont.rgbBlue  = 255 - cont.rgbBlue
        
    def __getSize(self, bitmap):
        """
        """
        return FISize( self.__lib.GetWidth(bitmap), self.__lib.GetHeight(bitmap) )
    
    def __ctrlColorUsed(self):
        """
        """
        caller = "FreeImage_%s" % sys._getframe(1).f_code.co_name
        locals = sys._getframe(1).f_locals
        if not 'bitmap' in locals: return
        bitmap = locals['bitmap']
        for funct in FUNCTION_LIST:
            functName = funct[0]
            
            #Colour depth Control 
            if caller == functName and len(funct) > 2:
                colorUsed = funct[2]
                bpp = self.GetBPP(bitmap)
                if not bpp in colorUsed:
                    
                    #Unload at least the bitmap and the library
                    try: self.Unload(bitmap)
                    except: pass
                    try: self.DeInitialise()
                    except: pass
                    
                    #Raise an exception
                    raise FreeImagePy_ColorWrong, (
                        'Wrong color %s in function: %s. I can use: %s. Bitmap: %s' %
                        (bpp, functName, colorUsed, bitmap) )
                break
            
            #No control need, go out and save cpu time
            elif caller == functName: 
                break
        
    def __ctrlInit(self):
        """ Control if I call the init
        """
        pass
    
    def __closeIf(self, bitmap, close):
        """ Help method for internal close arg
            A lot of my functions need a simple
            but very annoing code, so I was create...
            
            My use:  self.__closeIf(bitmap, close)
        """
        
        if close:
            self.Unload(bitmap)

    library = property(GetLibrary)
    version = property(GetVersion)
    
#Image class, like PIL :)

class Image(freeimage):
    """
    FreeImagePy Image class. Use me like I'm a PIL Image class.
    
    Here you not need to pass me every time the dib istance, because 
    it'll remember the dib alone:
    
    freeimage class (old method):
        import FreeImagePy as FIPY
        F = FIPY.freeimage()
        dib = F.genericLoader("mypath.png")
        newD = F.RotateClassic(dib, 90)
        F.save(FIF_TIFFG4, "new_path.png", newD)
        F.Unload(dib)
        F.Unload(newD)
    
    Image class (new):
        import FreeImagePy as FIPY
        F = FIPY.Image("mypath.png")
        newI = F.rotate(90)
        newI.save("mypath.tiffg4") # save a mypath.tiff with g4 compression
        del I, newI
        
    @author: Michele Petrazzo
    """
    
    def __init__(self, f=None, libraryName=None):
        """ Costrunct class
        @see: freeimage __init__
        """
        self.__libraryName = libraryName
        self.__bitmap = None
        self.__unloadWhenDel = True
        self.__format = None
        self.__fileName = ""
        self.__automaticColorChange = True
        self.index = 1
        
        #MultiPage
        self.__bitmapMulti = None
        self.__isMultipage = False
        
        super(Image, self).__init__(libraryName)
        
        #If need, load the page
        if f: self.load(f)
            
    def load(self, fileName, unloadPrev=True, try_multiPage=True):
        """ Load the filename
        @param fileName: File name path
        @type fileName: string
        """
        if unloadPrev: self.__unload(0)
        self.__fileName = fileName

        self.__isMultipage = False
        self.__numPages = 1

        ret_val, pageNum = self.isMultiPage(fileName)
        if try_multiPage and not ret_val:
            self.__isMultipage = True
            self.__numPages = pageNum
            self.__bitmapMulti = self.openMulti(fileName)
            self.__bitmapMultiCurrentNumber = 0
            self.__bitmap = self.LockPage(self.__bitmapMulti,
                            self.__bitmapMultiCurrentNumber)
        else:
            self.__bitmap = self.genericLoader(fileName)
        #If I load correcly the bitmap
        if self.__bitmap:
            #set its the format
            self.__setFormat()
        else:
            warn("I cannot load the bitmap at: %s" % fileName, TypeNotFound)
            return 1

    def loadFromBitmap(self, bitmap, unloadPrev=True):
        """ Load an already loaded bitmap. Useful when you have to use
            some functions that this class hasn't bind.
            @param bitmap: An already loaded bitmap (Useful for the old class style)
            @type bitmap: int
            @param unloadPrev: Uload the previous bitmap if there is one
            @type unloadPrev: True/False
        """
        if unloadPrev: self.__unload(0)
        self.__fileName = "Clone bitmap, no filename provided"
        self.__bitmap = bitmap
        self.__setFormat()
    
    def new(self, size=None, bpp=24, white=True, unloadPrev=True, 
            multiBitmap=None, fileType=None, flags=0):
        """ Create a new image with the given FISize and with that BPP
            
            @param size: The new bitmap size. Can be none if the bitmap are a multipage
            @type size: FISize (w,h) or two value tuple
            @param bpp: color depth
            @type bpp:  in (1 -> 32)
            @param white: If True, I return a white image
            @type white: True/False
            @param multiBitmap: multiBitmap path for the new image
            @type multiBitmap: string
            @param fileType: FIF_*
        """
        if unloadPrev: self.__unload(0)
        
        if size == None:
            if not multiBitmap:
                raise ValueError, "You have to specify at least the size or a multiBitmap path"
            size = (1,1)
        
        w,h = size
        
        if multiBitmap:
            if not fileType: fileType = FIF_TIFF
            
            self.__isMultipage = True
            self.__numPages = 1
            self.__bitmapMultiCurrentNumber = 0
            self.__fileName = multiBitmap
            
            self.__bitmapMulti = self.OpenMultiBitmap(fileType, 
                        multiBitmap, True, flags=flags)
            
            #Create the empty image
            i = Image()
            i.new(size, bpp, white)
            
            #append it
            self.AppendPage(self.__bitmapMulti, i.bitmap)
            del i
            self.CloseMultiBitmap(self.__bitmapMulti)
            
            self.__bitmapMulti = self.OpenMultiBitmap(fileType, 
                        multiBitmap)
            self.__bitmap = self.LockPage(self.__bitmapMulti, 0)
            
        else:
            dib = self.Allocate(w,h, bpp)
            self.__bitmap = dib
        
        #Invert if need
        if white: self.invert()
        self.__setFormat()
        
    
    def save(self, fileName, type=None, flags=False):
        """Save the current already loaded bitmap
            
            @param fileName: File name path. If fileName has extension, and
                not type are specified, try to learn the type from extension
            @type fileName: string
            @param type: a extToType key or a FIF type
            @type type: int/string 
            @param flags: some -type specific- flags 
            @type flags: int
        """
        
        ret = getParametersFromExt(fileName, type)
        if not ret:
            warn("Type %s not found in FIFTotype dict when save. See the docs" % type, TypeNotFound)
            return 1
        else:
            FIF, ext, flag, fileName = ret
            if not flags: flags = flag
            
        return self.Save(FIF, self.__bitmap, fileName, flags)
    
    def close(self):
        """ Close the loaded bitmap
        """
        self.__unload(closing=True)
        return
    
    def exit(self):
        """ Close the bitmap and unload the library
        """
        self.__unload(closing=True)
        self.DeInitialise()
    
    #
    #Size methods
    #
    
    def getSize(self):
        """ Return the bitmap size
        @return: FISize (w,h)
        """
        return super(Image, self).getSize(self.__bitmap)
    
    def setSize(self, size, filter=FILTER_BSPLINE, inplace=True):
        """ Property size method
        @param size: new bitmap size
        @type size: FISize or a tuple (w,h)
        """
        w, h = size
        if int(w) == 0 or int(h) == 0:
           raise ValueError, "You cannot pass me null values: %s " % str(size)
        self.resize(size, filter, inplace)
        self.__setFormat()
            
    def resize(self, size, filter=FILTER_BSPLINE, inplace=True):
        """ Set the image size. If inplace is True I'll resize the current bitmap
            If not inplace, pay attention to keep the bitmap istance and delete it
            when no longer used.
            @param size: new bitmap size
            @type size: FISize or a tuple (w,h)
            @param filter: filter type, see FILTER_*
            @type filter: int
            @param inplace: Resize inplace or not the bitmap
            @type inplace: True o False
        """
        
        newBppifNeed = 24
        oldBpp = self.GetBPP(self.__bitmap)
        
        #If I have to change color
        if self.__automaticColorChange:
            #and I need to do it...
            if oldBpp not in (COL_8, COL_24, COL_32):
                self.__bitmap = self.setBppFromBpp(newBppifNeed, self.__bitmap)
        w, h = size
        new_bitmap = self.Rescale(self.__bitmap, w, h, filter, inplace)
        
        #If I need to re-change the color
        if self.GetBPP(new_bitmap) != oldBpp:
            new_bitmap = self.setBppFromBpp(oldBpp, new_bitmap)

        #If in place
        if inplace: self.__bitmap = new_bitmap
    
    def thumbnail(self, max_pixel_size, convert=True, close=0):
        """ Make an image thumbnail and return a new image
            Pay attention to set close arg 0!
        """
        bmp = self.MakeThumbnail(self.__bitmap, max_pixel_size, convert, close)
        
        img = Image()
        img.loadFromBitmap(bmp)
        return img
    
    #
    #Help methods
    #
    
    def getStatus(self):
        """ Return the library status
        """
        return super(Image, self).getStatus()
    
    def ok(self):
        """ Return if the bitmap and its associated library istance status
            @return: string
        """
        if self.__bitmap: 
            return 0, ("Bitmap: %s. loaded at %s ok" % (self.__fileName, self.__bitmap) )
        else:
            return 1, "Bitmap: %s, NOT OK" % self.__fileName
    
    def convertToMinIsWhite(self, invert=True):
        """ Convert the current bitmap to MINISWHITE.
            @param invert: If False, I only invert the palette
            @type invert: True/False
        """
        if invert:
            super(Image, self).convertToMinIsWhite(self.__bitmap)
        else:
            super(Image, self).convertPaletteToMinIsWhite(self.__bitmap)
        self.__setFormat()
        
    def setColorUsed(self, bpp):
        """ Change the depth color for this bitmap
            @param bpp: New depth
            @type bpp: int (1,4,8,16,32)
        """
        self.__bitmap = self.setBppFromBpp(bpp, self.__bitmap)
        self.__setFormat()
    
    def getColorUsed(self):
        """ Return the color used 
            @return int
        """
        return self.GetColorsUsed(self.__bitmap)
    
    def getBPP(self):
        """ Return the bpp
            @return int
        """
        return self.GetBPP(self.__bitmap)
    
    #
    #Bitmap access methods
    #
    
    def getBitmap(self):
        """ Return the current bitmap dib
            @return: int
        """
        return self.__bitmap
    
    def setBitmap(self, bitmap):
        """ Set the current bitmap dib
            @param bitmap: An Image istance or an "old" bitmap dib
            @type bitmap: Image istance or int
        """
        self.__bitmap = self.__getBitmapDib(bitmap)
    
    def getFormat(self):
        """ Return the bitmap format
        @return: (FIF type, FIC type) -> Example: (TIFF, RGB)
        """
        return self.__format
    
    def getFileName(self):
        """ Return the bitmap filename path (when load)
            @return: string file name
        """
        return self.__fileName
    
    #
    #Multipage
    #
    
    def isMulti(self):
        """ Return if the bitmap loaded is a multipage dib 
            @return: int
        """
        return self.__isMultipage
    
    def getNumPages(self):
        """ Return the current bitmap page numbers
            @return: int
        """
        if not self.__isMultipage: return 1
        return self.GetPageCount(self.__bitmapMulti)
    
    def getCurrentPage(self):
        """ Return the current page number
            @return: int
        """
        
        if not self.__isMultipage: return 1
        return self.__bitmapMultiCurrentNumber
    
    def setCurrentPage(self, pageNum=0):
        """ Set the current page number. 
            If yor seek outside the image sequens, raise EOFError
            
            @param pageNum: The page to laod into a multi-page environ
            @type pageNum: Int
        """
        if not self.__isMultipage or \
            pageNum == self.__bitmapMultiCurrentNumber: return False
        
        #Control for the end of bitmaps
        if pageNum > self.__numPages -1: raise EOFError, "No more pages"
        
        #Close the page and open the new one
        self.UnlockPage(self.__bitmapMulti, self.__bitmap)
        self.__bitmap = self.LockPage(self.__bitmapMulti, pageNum)
        self.__bitmapMultiCurrentNumber = pageNum
        
        #Set the right index
        self.index = pageNum +1
        
    def seek(self, page=0):
        """ Seek method.
            @see: setCurrentPage
        """
        return self.setCurrentPage(page)
    
    def tell(self):
        """Tell method
            @see: getCurrentPage
        """
        return self.getCurrentPage()
    
    def appendPage(self, fileName=None, bitmap=None, insert=None):
        """ Append new page from an already loaded bitmap or from a filename. If
            insert is an int, insert the image into that position        
            
            @param bitmap: an Image istance or an "old" bitmap or None
            @param fileName: filename path or None
            @type insert: int or None. If int I'll insert the bitmap at insert number            
        """
        if not self.__isMultipage: return False
        
        if fileName:
            bitmap = self.genericLoader(fileName)
        elif bitmap:
            bitmap = self.__getBitmapDib(bitmap)
        else:
            raise AttributeError, "You must pass me one parameter!"
        
        pl = self._getPagesLock()
        if pl: self.UnlockPage(self.__bitmapMulti, self.__bitmap, True)
        
        #If insert need
        if insert != None:
            self.InsertPage(self.__bitmapMulti, insert, bitmap)
            self.__bitmapMultiCurrentNumber = insert
        else:
            self.AppendPage(self.__bitmapMulti, bitmap)
            self.__bitmapMultiCurrentNumber += 1
        
        #Reflect the changes to the multi-page file. I need it because
        #freeimage need it!
        self.CloseMultiBitmap(self.__bitmapMulti)
        self.__bitmapMulti = self.openMulti(self.__fileName)

        self.__numPages = self.GetPageCount(self.__bitmapMulti)
        self.__bitmap = self.LockPage(self.__bitmapMulti, 
                self.__bitmapMultiCurrentNumber)
        
        return True
        
    def deletePage(self, pageNum):
        """ Delete the page passed as value
            @param pageNum: Page number
            @type pageNum: int
        """
        if not self.__isMultipage: return False

        pl = self._getPagesLock()
        if pl: self.UnlockPage(self.__bitmapMulti, self.__bitmap, True)
        retDel = self.DeletePage(self.__bitmapMulti, pageNum)
        
        #reflect the changes
        self.CloseMultiBitmap(self.__bitmapMulti)
        self.__bitmapMulti = self.openMulti(self.__fileName)
        
        self.__numPages = self.GetPageCount(self.__bitmapMulti)
        
        if self.__numPages != 0:
            self._lockPage(self.__numPages-1)
        return retDel
    
    def convertToPages(self, fileOut, extType=None):
        """ Convert the multipage dib loaded into single pages
            
            @param fileOut: the output filename.
            @type fileOut: string
            @param extType: strings indicate the extension or int the type (FIF_*)
            @type extType: str or int
        """
        fileNames = list()
        if not self.__isMultipage: return fileNames
        
        pl = self._getPagesLock()
        if pl: self.UnlockPage(self.__bitmapMulti, self.__bitmap, True)

        ret = getParametersFromExt(fileOut, extType)
        if not ret:
            warn("Type %s not found in FIFTotype dict when save. See the docs" % 
                extType, TypeNotFound)
            return 1
        FIF, ext, flags, fileOut = ret
        
        for p in xrange(self.getNumPages()):
            outputName, ext = os.path.splitext(fileOut)
            fileNameOut = '%s%s%s' % (outputName, p, ext)
            fileNames.append(fileNameOut)
            
            dib = self.LockPage(self.__bitmapMulti, p)
            self.Save(FIF, dib, fileNameOut, flags)
            self.UnlockPage(self.__bitmapMulti, dib)
            
        return fileNames
    
    #
    #Pixel
    #

    def getPixel(self, point):
        """ Return the pixel value
            @param point: The points for find the pixel value
            @type point: FIPoint or tuple (x,y)
        """
        if self.GetBPP(self.__bitmap) in COL_1TO8:
            funct = self.GetPixelIndex 
        else:
            funct = self.GetPixelColor
        x,y = point
        return funct(self.__bitmap, x,y)
    
    def getBuffer(self, close=0, topdown=False):
        """ Retrun the bitmap buffer
            @return: buffer
        """
        return super(Image, self).getBuffer(self.__bitmap, close, topdown)
    
    def fromBuffer(self, buff, fif=None, flag=0, unloadPrev=True):
        """ Load a buffer and (try) to convert it to a dib.
            @param buff: The buffer
            @type buff: string
        """
        if unloadPrev: self.__unload(0)
        self.__bitmap = super(Image, self).loadFromBuffer(buff, fif, flag)
    
    #
    #Copy / Clone / Paste
    #
    
    def clone(self):
        """ Clone the current bitmap
            @return: new Image istance
        """ 
        return self.__newIstance( self.Clone(self.__bitmap) )
    
    def copy(self, left, top, right, bottom, unloadPrev=False):
        """ Copy a sub part of the current dib image, return a new Image
            @param left, top, right, bottom: The image rectangle to copy
            @type left, top, right, bottom: int
            @return: New bitmap istance
        """
        new_img = self.Copy(self.__bitmap, left, top, right, bottom)
        if unloadPrev: self.__unload(self.__bitmap, 0)
        return self.__newIstance(new_img)
    
    def paste(self, bitmap, box=None, alpha=255):
        """ Paste an image passed into this image
        @param bitmap: The bitmap where copy
        @param box: The box size
        @type box: - None -> start to paste at (0,0)
                   - FIPoint (left, top) -> start to past at (left, top)
                   - Four values tuple (left, top, right, bottom) paste 
                        AND resize if need the source bitmap. 
                        I clone the image before resize it
        @param alpha:
        @type alpha:
        """
        
        dibInst = self.__getBitmapIstance(bitmap)
        dib = self.__getBitmapDib(bitmap)
        
        if box == None:
            l, t = 0, 0
        elif len(box) == 2:
            l, t = box
        else:
            l, t, right, bottom = box
            sourceEndSize = FISize(right - l, bottom - t)
            if not (dibInst.size.w == sourceEndSize.w and \
                dibInst.size.h == sourceEndSize.h):
                    dibInst = dibInst.clone()
                    dibInst.size = sourceEndSize
                    dib = dibInst.bitmap
        return self.Paste(self.__bitmap, dib, l, t, alpha)
    
    #
    #Color
    #
    
    def invert(self):
        """ Invert the bitmap colors in place
        """
        self.Invert(self.__bitmap)
    
    def GetHistogram(self):
        """ Return image histogram
        """
        dHistogram = dict()
        for channel, ch_name in (
                (FICC_BLACK, "black"), (FICC_RED, "red"),
                (FICC_GREEN, "green"),(FICC_BLUE, "blue"),):
            
            DW_256 = DWORD * 256 # type
            histo = DW_256()
            super(Image, self).GetHistogram(self.__bitmap, C.byref(histo), channel)
            
            dHistogram[ch_name] = [int(x) for x in histo]
            
        return dHistogram

    def GetBackgroundColor(self):
        """ Return the background color, if any. Otherwise I'll return 0
            @return: 0 (if no bg color) or (R,G,B)
        """
        if super(Image, self).HasBackgroundColor(self.__bitmap):
            return super(Image, self).GetBackgroundColor(self.__bitmap)
        else:
            return 0
        
    def SetBackgroundColor(self, color):
        """ Set background color.
            @par color: dict with red, green, blue keys
            @type color: dict
        """
        super(Image, self).SetBackgroundColor(self.__bitmap, color)
    
    def GetTransparent(self):
        """
        """
        return super(Image, self).IsTransparent(self.__bitmap)
        
    def SetTransparent(self, value):
        """
        """
        return super(Image, self).SetTransparent(self.__bitmap, value)
        
    #
    #Rotation and flipping
    #
    
    def rotate(self, angle, inplace=False):
        """ Rotate the bitmap and return the new one if inplace are False
            @param angle: The angle to rotate
            @type angle: int
            @param inplace: Rotate the image inplace
            @type inplace: int
        """
        
        new_dib = self.RotateClassic(self.__bitmap, angle, inplace)
        if inplace:
            self.__unload()
            self.__bitmap = new_dib
        else:
            newinst = self.__newIstance(new_dib)
            #Need because freeimage "forgot" the palette
            newinst.convertToMinIsWhite(False)
            return newinst
    
    #
    # Bitmap information
    #
    
    def getBPP(self):
        """ Get the bpp (size of one pixel in the bitmap in bits)
            @return: int
        """
        return super(Image, self).GetBPP(self.__bitmap)
        
    def setBPP(self, bpp):
        """ Set the bpp value
            
            @param bpp: The new bpp value
            @type bpp: int
        """
        self.__bitmap = super(Image, self).setBppFromBpp(bpp, self.__bitmap)
    
    #
    #Metadata
    #
    
    def GetMetadataCount(self):
        """ Count metadata for this model
        """
        metaCount = dict()
        for k, d in FIMD__METALIST.iteritems():
            count = super(Image, self).GetMetadataCount(d, self.__bitmap)
            metaCount[k] = count
        return metaCount
    
    def getMetadata(self):
        """ Return the matadata data this image has inside
        """
        meta = dict()
        
        for k, d in FIMD__METALIST.iteritems():    
            
            data = dict()
            
            tag = VOID()
            handle = super(Image, self).FindFirstMetadata(d, self.__bitmap, tag)
            
            if not tag.value: continue
            
            tts, td, tk = self._metaData(d, tag.value)
            data[tk] = tts
            

            while super(Image, self).FindNextMetadata(handle, tag):
                tagId = tag.value
                if not tagId: break
                tts, td, tk = self._metaData(d, tagId)
                data[tk] = tts
                #print k, tk, tts, tag.value
            
            super(Image, self).FindCloseMetadata(handle)
            
            meta[k] = data
        
        return meta
            
    #
    # Pil compatibility methods
    #
    
    def convertToPil(self):
        """ Convert the current Image to PIL image, if PIL is installed
            
            @return: PIL istance or None if PIL is not installed
        """
        return convertToPil(self)

    #
    # Wx compatibility methods
    #
    
    def convertToWx(self):
        """ Covnert the current Image to PIL image, if PIL is installed
            
            @return: PIL istance or None if PIL is not installed
        """
        return convertToWx(self)

    #
    # Close methods
    # 
    
    def getUnloadWhenDel(self):
        """ Return if I have to delete the bitmap when close
        """
        return self.__unloadWhenDel
    
    def setUnloadWhenDel(self, value):
        """ Set the unloadWhenDel attribute
        @param value: The value
        @type value: True or False
        """
        self.__unloadWhenDel = value
    
    #
    #Internal methods
    #
    
    def _lockPage(self, page):
        """ Lock the page passed
            @param page: Number of page
            @type page: Int
        """
        pl = self._getPagesLock()
        if pl: self.UnlockPage(self.__bitmapMulti, self.__bitmap, True)
        
        self.__bitmapMultiCurrentNumber = page
        self.__bitmap = self.LockPage(self.__bitmapMulti, page)

    def _getPagesLock(self):
        """ Return the pages locked
        """
        return self.GetLockedPageNumbers(self.__bitmapMulti)
        
    def __getBitmapDib(self, bitmap):
        """ Opposite to __getBitmapIstance
        """
        if hasattr(bitmap, "bitmap"): dib = bitmap.bitmap
        else: dib = bitmap
        return dib
        
    def __getBitmapIstance(self, bitmap):
        """ Need when a user pass me an "old" dib istance
        """
        if hasattr(bitmap, "bitmap"): dib = bitmap
        else: 
            dib = Image()
            dib.loadFromBitmap(bitmap)
        return dib
    
    def __newIstance(self, bitmap):
        """Create a new birmap istance and return it
        """
        new_inst = Image(self.__libraryName)
        new_inst.loadFromBitmap(bitmap)
        return new_inst
    
    def __setFormat(self):
        """ Set the format attribute
        """
        FIF, FIC = ( self.genericFileDeducer(self.__fileName), 
                     self.GetColorType(self.__bitmap) )
        formatCode  = FIF, FIC
        formatDescr = FIFTotype[FIF], FICTotype[FIC] 
        dpi = self.getDotDPI(self.__bitmap)
        self.__format = (formatCode, formatDescr, dpi)
        
    def __unload(self, ctrlVal=True, closing=None):
        """ Help method for unload bitmap
        """
        if closing and self.__isMultipage:
            #unlock the pages and save the modifies
            
            for p in self._getPagesLock():
                self.UnlockPage(self.__bitmapMulti, self.__bitmap, True)
            self.__bitmap = None
            self.CloseMultiBitmap(self.__bitmapMulti)
            return

        if closing and self.__bitmap:
            self.Unload(self.__bitmap)
            self.__bitmap = None
            return
        
        if self.__bitmap and (self.__unloadWhenDel and ctrlVal):
            if self.__isMultipage:
                self.UnlockPage(self.__bitmapMulti, 
                    self.__bitmapMultiCurrentNumber, modified=True)
            else:
                self.Unload(self.__bitmap)
            self.__bitmap = None

    def _metaData(self, model, tagId):
        """ Pass me a model and and tag id, I'll return the:
            TagToString
            GetTagDescription
            GetTagKey
        """
        tts, td, tk = (super(Image, self).TagToString(model, tagId),
                    super(Image, self).GetTagDescription(tagId),
                    super(Image, self).GetTagKey(tagId))
        
        
        #TODO: Another solution for retrieve the metadata...
        #Why?
        
        #myTag = super(Image, self).GetMetadata(model, self.__bitmap, tk)
        #tv = super(Image, self).GetTagValue(myTag)
        
        return (tts, td, tk)
        
        
    def __del__(self):
        """ Implicit unload the bitmap
        """
        self.__unload(closing=False)
        #self.exit()
    
    def __repr__(self):
        """
        """
        return "Library istance: %s.\nImage instance: %s" % \
            (self.getStatus(), self.ok() )
    
    def __iter__(self):
        """ Iterate over a multipage dib
        """
        return self
    
    def next(self):
        """
        """
        if self.index -1 == self.numPages:
            raise StopIteration
        
        self.setCurrentPage(self.index -1)
        self.index += 1
        return self

    # --------------------- #
    #  Property definitions #
    # --------------------- #
    
    status = property(getStatus)
    size = property(getSize, setSize)
    bitmap = property(getBitmap, setBitmap)
    unloadWhenDel = property(getUnloadWhenDel, setUnloadWhenDel)
    format = property(getFormat)
    filename = property(getFileName)
    numPages = property(getNumPages)
    currentPage = property(getCurrentPage, setCurrentPage)
    bpp = property(getBPP, setBPP)
    metadata = property(getMetadata)
    histogram = property(GetHistogram)
    backgroundColor = property(GetBackgroundColor, SetBackgroundColor)
    transparent = property(GetTransparent,SetTransparent)
    
