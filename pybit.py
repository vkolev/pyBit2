#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Tue Sep  1 21:39:00 2009
#
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import wx
import urllib
import gtk
from configobj import ConfigObj
import commands

# Read the configuration file
config = ConfigObj("pybit.conf")
engine = int(config['engine'])
bituser = config['bitusername']
apiKey = config['api']
tuser = config['tusername']
tpass = config['tpassword']
site = config['siteaddres']

areaList = ["bit.ly", "is.gd", "smsh.me", "cli.gs", "tr.im"]
#areaList = ["bit.ly", "is.gd", "smsh.me", "cli.gs"]
# begin wxGlade: extracode
# end wxGlade

ID_TWITT = wx.NewId()
ID_CLEAR = wx.NewId()
ID_PREFS = wx.NewId()
ID_ABOUT = wx.NewId()
ID_EXIT = wx.NewId()

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.ICONIZE|wx.CAPTION|wx.MINIMIZE|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.MAXIMIZE_BOX|wx.SYSTEM_MENU|wx.RESIZE_BORDER|wx.CLIP_CHILDREN
        wx.Frame.__init__(self, *args, **kwds)
        self.sizer_2_staticbox = wx.StaticBox(self, -1, "The long long url: ")
        
        # Tool Bar
        self.frame_1_toolbar = wx.ToolBar(self, -1)
        self.SetToolBar(self.frame_1_toolbar)
        if "twitter" in site:
            self.frame_1_toolbar.AddLabelTool(ID_TWITT, "Twitt", wx.Bitmap("icons/tweet.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Send message to twitter", "")
        else:
            self.frame_1_toolbar.AddLabelTool(ID_TWITT, "StatusNet", wx.Bitmap("icons/laconic.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Send message to StatusNet based website", "")
        self.frame_1_toolbar.AddSeparator()
        self.frame_1_toolbar.AddLabelTool(ID_CLEAR, "Clear", wx.Bitmap("icons/clear.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Clear", "")
        self.frame_1_toolbar.AddLabelTool(ID_PREFS, "Preferences", wx.Bitmap("icons/preferences.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Settings", "")
        self.frame_1_toolbar.AddLabelTool(ID_ABOUT, "About", wx.Bitmap("icons/about.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "About pyBit", "")
        self.frame_1_toolbar.AddSeparator()
        self.frame_1_toolbar.AddLabelTool(ID_EXIT, "Exit", wx.Bitmap("icons/exit.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Exit PyBit", "")
        # Tool Bar end
        self.bitmap_1 = wx.StaticBitmap(self, -1, wx.Bitmap("icons/pybit-logo.png", wx.BITMAP_TYPE_ANY))
        self.text_ctrl_1 = wx.TextCtrl(self, -1, "")
        self.bitmap_button_1 = wx.BitmapButton(self, -1, wx.Bitmap("icons/OK.png", wx.BITMAP_TYPE_ANY))
        self.label_1 = wx.StaticText(self, -1, "Shorted:")
        self.text_ctrl_2 = wx.TextCtrl(self, -1, "", style=wx.TE_READONLY)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_TOOL, self.on_twitt_it, id=ID_TWITT)
        self.Bind(wx.EVT_TOOL, self.on_clear, id=ID_CLEAR)
        self.Bind(wx.EVT_TOOL, self.on_preferences, id=ID_PREFS)
        self.Bind(wx.EVT_TOOL, self.on_about, id=ID_ABOUT)
        self.Bind(wx.EVT_TOOL, self.on_exit_app, id=ID_EXIT)
        self.Bind(wx.EVT_BUTTON, self.on_short_it, self.bitmap_button_1)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("pyBit")
        _icon = wx.EmptyIcon()
        _icon.CopyFromBitmap(wx.Bitmap("icons/icon.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.SetSize((493, 386))
        self.frame_1_toolbar.Realize()
        self.text_ctrl_1.SetMinSize((410, 60))
        self.text_ctrl_1.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.text_ctrl_1.SetToolTipString("Enter a valid URL (e.g. 'http://')")
        self.bitmap_button_1.SetToolTipString("Shorten the URL!")
        self.bitmap_button_1.SetSize(self.bitmap_button_1.GetBestSize())
        self.label_1.SetFont(wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.text_ctrl_2.SetMinSize((388, 60))
        self.text_ctrl_2.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.text_ctrl_2.Enable(True)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.StaticBoxSizer(self.sizer_2_staticbox, wx.HORIZONTAL)
        sizer_1.Add(self.bitmap_1, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_2.Add(self.text_ctrl_1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_2.Add(self.bitmap_button_1, 0, wx.ALIGN_CENTER_VERTICAL|wx.SHAPED, 0)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        sizer_3.Add(self.label_1, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_4.Add(self.text_ctrl_2, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_3.Add(sizer_4, 1, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_1.Add(sizer_3, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        self.Centre()
        # end wxGlade

    def on_short_it(self, event): # wxGlade: MyFrame.<event_handler>
        long_url = self.text_ctrl_1.GetValue()
        if long_url == "":
            nte = wx.MessageDialog(None, "Sorry, no url enetered", "Warning!", wx.ID_OK | wx.ICON_WARNING )
            nte.ShowModal()
        elif self.url_checker(long_url) == 0:
            nvu = wx.MessageDialog(None, "Sorry, not valid url enetered", "Warning!", wx.ID_OK | wx.ICON_WARNING )
            nvu.ShowModal()
        else:
            if engine == 0:
                short_url = self.short_bitly(long_url, bituser, apiKey)
            elif engine == 1:
                short_url = self.short_isgd(long_url)
            elif engine == 2:
                short_url = self.short_smsh(long_url)
            elif engine == 3:
                short_url = self.short_cligs(long_url, apiKey)
            elif engine == 4:
                short_url = self.short_trim(long_url)
            else:
                unp = wx.MessageDialog(None, "Unknow problem accured!", "Error", wx.ID_OK | wx.ICON_ERROR )
                
            # Copy the short URL to the clipboard
            self.text_ctrl_2.SetValue(short_url)
            clipboard = gtk.clipboard_get()
            clipboard.set_text(short_url)
            clipboard.store()

    def on_twitt_it(self, event): # wxGlade: MyFrame.<event_handler>
        self.twitt_dialog = MyTwittDialog(None, -1, "")
        self.twitt_dialog.Show()

    def on_clear(self, event): # wxGlade: MyFrame.<event_handler>
        self.text_ctrl_1.SetValue("")
        self.text_ctrl_2.SetValue("")
        
    def on_preferences(self, event): # wxGlade: MyFrame.<event_handler>
        self.prefs_frame = PreferencesFrame(None, -1, "")
        self.prefs_frame.Show()

    def on_about(self, event): # wxGlade: MyFrame.<event_handler>
        self.about_dialog = MyAboutDialog(None, -1, "")
        self.about_dialog.Show()
        
    def on_exit_app(self, event):
        self.Destroy()

    def short_bitly(self, long_url, login_user, api_key):
        try:
            longUrl = urllib.urlencode(dict(longUrl=long_url))
            logIn = urllib.urlencode(dict(login=login_user))
            apiKey = urllib.urlencode(dict(apiKey=api_key))
            encodedurl = "http://api.bit.ly/shorten?version=2.0.1&%s&%s&%s" % (longUrl, logIn, apiKey)
            request = urllib.urlopen(encodedurl)
            responde = request.read()
            request.close()
            responde_dict = eval(responde)
            short_url = responde_dict['results'][long_url]['shortUrl']
            return short_url
        except IOError, e:
            errormess = wx.MessageDialog(None, "%s" % e, "Error!", wx.ID_OK | wx.ICON_ERROR )
            errormess.ShowModal()
            
    def short_isgd(self, long_url):
        try:
            longUrl = urllib.urlencode(dict(longurl=long_url))
            encodedurl = "http://is.gd/api.php?%s" % longUrl
            request = urllib.urlopen(encodedurl)
            responde = request.read()
            request.close()
            return responde
        except IOError, e:
            errormess = wx.MessageDialog(None, "%s" % e, "Error!", wx.ID_OK | wx.ICON_ERROR )
            errormess.ShowModal()
            
    
    def short_smsh(self, long_url):
        try:
            longUrl = urllib.urlencode(dict(longurl=long_url))
            encodedurl = "http://smsh.me/?api=json&url=%s" % longUrl
            request = urllib.urlopen(encodedurl)
            responde = request.read()
            request.close()
            responde_dict = eval(responde)
            short_url = responde_dict['body']
            return short_url
        except IOError, e:
            errormess = wx.MessageDialog(None, "%s" % e, "Error!", wx.ID_OK | wx.ICON_ERROR )
            errormess.ShowModal()
            
    def short_cligs(self, long_url, api_key):
        try:
            longUrl = urllib.urlencode(dict(url=long_url))
            apiKey = urllib.urlencode(dict(key=api_key))
            encodedurl = "http://cli.gs/api/v1/cligs/create?%s&%s&appid=%s" % (longUrl, apiKey, "pybit")
            request = urllib.urlopen(encodedurl)
            responde = request.read()
            return responde
        except IOError, e:
            errormess = wx.MessageDialog(None, "%s" % e, "Error!", wx.ID_OK | wx.ICON_ERROR )
            errormess.ShowModal()
            
    def short_trim(self, long_url):
        try:
            longUrl = long_url
            encodedurl = "http://api.tr.im/v1/trim_simple?url=%s" % longUrl
            request = urllib.urlopen(encodedurl)
            responde = request.read()
            request.close()
            return responde
        except IOError, e:
            errormess = wx.MessageDialog(None, "%s" % e, "Error!", wx.ID_OK | wx.ICON_ERROR )
            errormess.ShowModal()
    def on_button3_clicked(self, widget):
        # Empties the text fields, so you can add short another URL
        self.entry.set_text("")
        self.entry2.set_text("")
        
    def url_checker(self, long_url):
        #checks if a correct URL is given
        # TODO: replace with regular expressions
        if "https://" in long_url and len(long_url) > 14:
            return 1
        elif "http://" in long_url and len(long_url) > 13:
            return 1
        elif "ftp://" in long_url and len(long_url) > 12:
            return 1
        else:
            return 0
# end of class MyFrame

class MyTwittDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyTwittDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.text_ctrl_3 = wx.TextCtrl(self, -1, "", style=wx.TE_MULTILINE)
        self.button_1 = wx.Button(self, wx.ID_CANCEL, "")
        self.button_2 = wx.Button(self, wx.ID_UP, "")
        self.button_3 = wx.Button(self, wx.ID_PASTE, "")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.close_twitter, self.button_1)
        self.Bind(wx.EVT_BUTTON, self.on_twitter_send, self.button_2)
        self.Bind(wx.EVT_BUTTON, self.add_url_to_text, self.button_3)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyTwittDialog.__set_properties
        self.SetTitle("pyBit : Status updater")
        _icon = wx.EmptyIcon()
        _icon.CopyFromBitmap(wx.Bitmap("icons/icon.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.SetSize((400, 192))
        self.text_ctrl_3.SetMinSize((400, 150))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyTwittDialog.__do_layout
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5.Add(self.text_ctrl_3, 0, wx.EXPAND, 0)
        sizer_6.Add(self.button_1, 0, 0, 0)
        sizer_6.Add(self.button_3, 0, 0, 0)
        sizer_6.Add(self.button_2, 0, 0, 0)
        sizer_5.Add(sizer_6, 1, wx.ALIGN_RIGHT, 0)
        self.SetSizer(sizer_5)
        self.Layout()
        # end wxGlade

    def close_twitter(self, event): # wxGlade: MyTwittDialog.<event_handler>
        self.Destroy()

    def add_url_to_text(self, event):
        # showld also be changed but for now it works - get's the last entry in the clipboard
        clipboard = gtk.clipboard_get()
        self.text_ctrl_3.AppendText(clipboard.wait_for_text())

    def on_twitter_send(self, event): # wxGlade: MyTwittDialog.<event_handler>
        message = self.text_ctrl_3.GetValue()
        if message == "":
            tsm = wx.MessageDialog(None, "Your message is empty!", "Warning", wx.ID_OK | wx.ICON_WARNING )
            tsm.ShowModal()
        elif len(message) > 140:
            tlm = wx.MessageDialog(None, "Your message is too long to be posted!", "Warning", wx.ID_OK | wx.ICON_WARNING )
            tlm.ShowModal()
        else:
            # the actual curl command to update the status
            curl = 'curl -s -u %s:%s -d status="%s" -d source="pyBit" %s' % (tuser,tpass,message,site)
            treturn = commands.getoutput(curl)
            if "Could not authenticate you." in treturn:
                ems = wx.MessageDialog(None, "There was a problem authenticating you.\n\nPlease check your username and password", "Error", wx.ID_OK | wx.ICON_ERROR)
                ems.ShowModal()
            elif "<created_at>" in treturn:
                sms = wx.MessageDialog(None, "Your status was updated!", "Send", wx.ID_OK | wx.ICON_INFORMATION )
                sms.ShowModal()
            else:
                uems = wx.MessageDialog(None, "There was an unknown problem sending your update", "Error", wx.ID_OK | wx.ICON_ERROR)
                uems.ShowModal()
            #pipe = popen(curl, 'r')
            #print pipe

# end of class MyTwittDialog


class PreferencesFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: PreferencesFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.sizer_17_staticbox = wx.StaticBox(self, -1, "Site url:")
        self.sizer_16_staticbox = wx.StaticBox(self, -1, "Status update")
        self.label_2 = wx.StaticText(self, -1, "Select Engine:")
        self.combo_box_1 = wx.ComboBox(self, -1, value=areaList[engine], choices=areaList, style=wx.CB_DROPDOWN|wx.CB_READONLY)
        self.label_3 = wx.StaticText(self, -1, "Bit.ly Username:")
        self.text_ctrl_5 = wx.TextCtrl(self, -1, "%s" % bituser)
        self.label_4 = wx.StaticText(self, -1, "Bit.ly apiKey:")
        self.text_ctrl_6 = wx.TextCtrl(self, -1, "%s" % apiKey)
        self.label_5 = wx.StaticText(self, -1, "Username:")
        self.text_ctrl_7 = wx.TextCtrl(self, -1, "%s" % tuser)
        self.label_6 = wx.StaticText(self, -1, "Password:")
        self.text_ctrl_8 = wx.TextCtrl(self, -1, "%s" % tpass, style=wx.PASSWORD)
        self.label_7 = wx.StaticText(self, -1, "URL:")
        self.text_ctrl_9 = wx.TextCtrl(self, -1, "%s" % site)
        self.button_5 = wx.Button(self, wx.ID_CLOSE, "")
        self.button_6 = wx.Button(self, wx.ID_SAVE, "")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.close_preferences, self.button_5)
        self.Bind(wx.EVT_BUTTON, self.save_settings, self.button_6)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: PreferencesFrame.__set_properties
        self.SetTitle("pyBit Preferences")
        _icon = wx.EmptyIcon()
        _icon.CopyFromBitmap(wx.Bitmap("icons/icon.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.SetSize((400, 306))
        self.text_ctrl_7.SetMinSize((100, 25))
        self.text_ctrl_8.SetMinSize((100, 25))
        self.text_ctrl_9.SetMinSize((300, 25))
        if engine == 1:
            self.text_ctrl_5.Enable(False)
            self.text_ctrl_6.Enable(False)
        elif engine == 2:
            self.text_ctrl_5.Enable(False)
            self.text_ctrl_6.Enable(False)
        elif engine == 3:
            self.text_ctrl_5.Enable(False)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: PreferencesFrame.__do_layout
        sizer_9 = wx.BoxSizer(wx.VERTICAL)
        sizer_18 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_17 = wx.StaticBoxSizer(self.sizer_17_staticbox, wx.HORIZONTAL)
        sizer_16 = wx.StaticBoxSizer(self.sizer_16_staticbox, wx.HORIZONTAL)
        sizer_14 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_15 = wx.BoxSizer(wx.VERTICAL)
        sizer_12 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_13 = wx.BoxSizer(wx.VERTICAL)
        sizer_10 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_11 = wx.BoxSizer(wx.VERTICAL)
        sizer_10.Add(self.label_2, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_11.Add(self.combo_box_1, 0, 0, 0)
        sizer_10.Add(sizer_11, 1, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_9.Add(sizer_10, 1, wx.EXPAND, 0)
        sizer_12.Add(self.label_3, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_13.Add(self.text_ctrl_5, 0, wx.EXPAND, 0)
        sizer_12.Add(sizer_13, 1, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_9.Add(sizer_12, 1, wx.EXPAND, 0)
        sizer_14.Add(self.label_4, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_15.Add(self.text_ctrl_6, 0, wx.EXPAND, 0)
        sizer_14.Add(sizer_15, 1, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_9.Add(sizer_14, 1, wx.EXPAND, 0)
        sizer_16.Add(self.label_5, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_16.Add(self.text_ctrl_7, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_16.Add(self.label_6, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_16.Add(self.text_ctrl_8, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_9.Add(sizer_16, 1, wx.EXPAND, 0)
        sizer_17.Add(self.label_7, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_17.Add(self.text_ctrl_9, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_9.Add(sizer_17, 1, wx.EXPAND, 0)
        sizer_18.Add(self.button_5, 0, 0, 0)
        sizer_18.Add(self.button_6, 0, 0, 0)
        sizer_9.Add(sizer_18, 1, wx.ALIGN_RIGHT, 0)
        self.SetSizer(sizer_9)
        self.Layout()
        # end wxGlade

    def close_preferences(self, event): # wxGlade: PreferencesFrame.<event_handler>
        self.Destroy()

    def save_settings(self, event): # wxGlade: PreferencesFrame.<event_handler>
        config['engine'] = self.combo_box_1.GetSelection()
        config['bitusername'] = self.text_ctrl_5.GetValue()
        config['api'] = self.text_ctrl_6.GetValue()
        config['tusername'] = self.text_ctrl_7.GetValue()
        config['tpassword'] = self.text_ctrl_8.GetValue()
        config['siteaddres'] = self.text_ctrl_9.GetValue()
        try:
            config.write()
            sd = wx.MessageDialog(None, "Settings saved successfully!\n\nPlease restart pyBit to apply the changes!", "Success", wx.ID_OK | wx.ICON_INFORMATION)
            sd.ShowModal()
        except:
            ud = wx.MessageDialog(None, "Problem saving settings", "Error", wx.ID_OK | wx.ICON_ERROR)
            ud.ShowModal()

# end of class PreferencesFrame

class MyAboutDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.bitmap_1 = wx.StaticBitmap(self, -1, wx.Bitmap("icons/icon.png", wx.BITMAP_TYPE_ANY))
        self.label_2 = wx.StaticText(self, -1, "About pyBit")
        self.label_3 = wx.StaticText(self, -1, "pyBit is an application for shortening URLs and also posting\nthem to twitter or identi.ca.\nIt supports 5 shortening engines:\n- bit.ly\n- is.gd\n- smsh.me\n- cli.gs\n- tr.im\n\nAuthor: Vladimir Kolev\nLicense: GNU/GPLv3\nLanguage: Python, WxWidgets\nYear: 2009")
        self.button_8 = wx.Button(self, -1, "http://pybit.vladimirkolev.com")
        self.button_8.SetForegroundColour(wx.Colour(0, 0, 255))
        self.Bind(wx.EVT_BUTTON, self.on_link_clicked, self.button_8)
        self.button_6 = wx.Button(self, wx.ID_CLOSE, "Close")
        self.Bind(wx.EVT_BUTTON, self.on_close_about, self.button_6)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyDialog.__set_properties
        self.SetTitle("About pyBit")
        _icon = wx.EmptyIcon()
        _icon.CopyFromBitmap(wx.Bitmap("icons/icon.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.Hide()
        self.label_2.SetFont(wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.label_3.SetMinSize((400, 180))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyDialog.__do_layout
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_6.Add(self.bitmap_1, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_6.Add(self.label_2, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_6.Add(self.label_3, 0, wx.EXPAND, 0)
        sizer_6.Add(self.button_8, 0, wx.EXPAND, 0)
        sizer_6.Add(self.button_6, 0, wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 0)
        self.SetSizer(sizer_6)
        sizer_6.Fit(self)
        self.Layout()
        # end wxGlade
        
    def on_close_about(self, event):
        self.Destroy()
        
    def on_link_clicked(self, event):
        webbrowser.open_new("http://pybit.vladimirkolev.com")
# end of class MyDialog

if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = MyFrame(None, -1, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()
