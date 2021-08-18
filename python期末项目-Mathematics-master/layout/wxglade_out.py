import wx

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.radio_box_1 = wx.RadioBox(self, wx.ID_ANY, u"运算类型选择", choices=[u"加法", u"减法", u"乘法", u"除法"], majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        self.radio_box_2 = wx.RadioBox(self, wx.ID_ANY, u"选择几步运算", choices=[u"一步", u"二步", u"三步"], majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        self.radio_box_3 = wx.RadioBox(self, wx.ID_ANY, u"题型设置", choices=[u"求结果", u"求算数项"], majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        self.button_1 = wx.Button(self, wx.ID_ANY, u"运行项及结果范围设置")
        self.button_2 = wx.Button(self, wx.ID_ANY, u"运算符号设置")
        self.checkbox_1 = wx.CheckBox(self, wx.ID_ANY, u"使用括号")
        self.radio_box_4 = wx.RadioBox(self, wx.ID_ANY, u"加法设置", choices=[u"随机进位", u"加法进位", u"没有进位"], majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        self.radio_box_5 = wx.RadioBox(self, wx.ID_ANY, u"减法设置", choices=[u"随机退位", u"减法退位", u"没有退位"], majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        self.text_ctrl_16 = wx.TextCtrl(self, wx.ID_ANY, "20", style=wx.TE_CENTRE)
        self.button_6 = wx.Button(self, wx.ID_ANY, u"添加口算题")
        self.button_7 = wx.Button(self, wx.ID_ANY, u"清空口算题")
        self.text_ctrl_1 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_2 = wx.TextCtrl(self, wx.ID_ANY, "5", style=wx.TE_CENTRE)
        self.text_ctrl_3 = wx.TextCtrl(self, wx.ID_ANY, "3", style=wx.TE_CENTRE)
        self.button_3 = wx.Button(self, wx.ID_ANY, u"设置口算卷子保存目录")
        self.text_ctrl_4 = wx.TextCtrl(self, wx.ID_ANY, u"小学生口算题")
        self.text_ctrl_5 = wx.TextCtrl(self, wx.ID_ANY, u"姓名：__________ 日期：____月____日 时间：________ 对题：____道", style=wx.TE_LEFT)
        self.button_8 = wx.Button(self, wx.ID_ANY, u"点此生成口算题打印文档")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("frame")
        self.radio_box_1.SetSelection(0)
        self.radio_box_2.SetSelection(0)
        self.radio_box_3.SetSelection(0)
        self.radio_box_4.SetSelection(0)
        self.radio_box_5.SetSelection(0)
        self.button_6.SetMinSize((160, 22))
        self.button_7.SetMinSize((160, 22))
        self.text_ctrl_1.SetMinSize((100, 40))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_14 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"卷子大标题小标题设置"), wx.HORIZONTAL)
        sizer_13 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"口算卷设置"), wx.HORIZONTAL)
        sizer_12 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"当前口算题包含内容"), wx.HORIZONTAL)
        sizer_11 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"添加口算题到卷子"), wx.VERTICAL)
        sizer_22 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_23 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"详细设置"), wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_24 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"运算项结果符号设置"), wx.HORIZONTAL)
        sizer_2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"口算题类型选择"), wx.HORIZONTAL)
        sizer_2.Add(self.radio_box_1, 0, 0, 0)
        sizer_2.Add(self.radio_box_2, 0, 0, 0)
        sizer_2.Add(self.radio_box_3, 0, 0, 0)
        sizer_1.Add(sizer_2, 0, wx.ALL | wx.EXPAND, 1)
        sizer_5.Add(self.button_1, 0, 0, 0)
        sizer_5.Add(self.button_2, 0, 0, 0)
        sizer_5.Add(self.checkbox_1, 0, 0, 0)
        sizer_4.Add(sizer_5, 1, wx.EXPAND, 0)
        sizer_24.Add(self.radio_box_4, 0, 0, 0)
        sizer_24.Add(self.radio_box_5, 0, 0, 0)
        sizer_4.Add(sizer_24, 1, wx.EXPAND, 0)
        sizer_3.Add(sizer_4, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_3, 0, wx.ALL | wx.EXPAND, 1)
        label_17 = wx.StaticText(self, wx.ID_ANY, u"口算题数：")
        sizer_22.Add(label_17, 0, 0, 0)
        sizer_22.Add(self.text_ctrl_16, 0, 0, 0)
        sizer_23.Add(self.button_6, 0, wx.ALL | wx.EXPAND, 0)
        sizer_23.Add(self.button_7, 0, wx.ALL | wx.EXPAND, 0)
        sizer_22.Add(sizer_23, 1, wx.EXPAND, 0)
        sizer_11.Add(sizer_22, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_11, 0, wx.ALL | wx.EXPAND, 1)
        sizer_12.Add(self.text_ctrl_1, 1, wx.ALL | wx.EXPAND, 0)
        sizer_1.Add(sizer_12, 1, wx.ALL | wx.EXPAND, 1)
        label_2 = wx.StaticText(self, wx.ID_ANY, u"生成卷子数量：")
        sizer_13.Add(label_2, 0, 0, 0)
        sizer_13.Add(self.text_ctrl_2, 0, wx.LEFT, 8)
        label_3 = wx.StaticText(self, wx.ID_ANY, u"口算题列数：")
        sizer_13.Add(label_3, 0, 0, 0)
        sizer_13.Add(self.text_ctrl_3, 0, 0, 0)
        sizer_13.Add(self.button_3, 0, 0, 0)
        sizer_1.Add(sizer_13, 0, wx.ALL | wx.EXPAND, 1)
        label_4 = wx.StaticText(self, wx.ID_ANY, u"卷子标题：")
        sizer_14.Add(label_4, 0, 0, 0)
        sizer_14.Add(self.text_ctrl_4, 0, 0, 0)
        label_5 = wx.StaticText(self, wx.ID_ANY, u"卷子副标题：")
        sizer_14.Add(label_5, 0, 0, 0)
        sizer_14.Add(self.text_ctrl_5, 1, wx.ALL, 0)
        sizer_1.Add(sizer_14, 0, wx.ALL | wx.EXPAND, 1)
        sizer_1.Add(self.button_8, 0, wx.ALL | wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

# end of class MyFrame

class MyDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyDialog.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.text_ctrl_6 = wx.TextCtrl(self, wx.ID_ANY, "0")
        self.text_ctrl_7 = wx.TextCtrl(self, wx.ID_ANY, "20")
        self.text_ctrl_8 = wx.TextCtrl(self, wx.ID_ANY, "0")
        self.text_ctrl_9 = wx.TextCtrl(self, wx.ID_ANY, "20")
        self.text_ctrl_10 = wx.TextCtrl(self, wx.ID_ANY, "0")
        self.text_ctrl_11 = wx.TextCtrl(self, wx.ID_ANY, "20")
        self.text_ctrl_12 = wx.TextCtrl(self, wx.ID_ANY, "0")
        self.text_ctrl_13 = wx.TextCtrl(self, wx.ID_ANY, "20")
        self.text_ctrl_14 = wx.TextCtrl(self, wx.ID_ANY, "0")
        self.text_ctrl_15 = wx.TextCtrl(self, wx.ID_ANY, "20")
        self.button_9 = wx.Button(self, wx.ID_ANY, u"提交修改")
        self.button_10 = wx.Button(self, wx.ID_ANY, u"关闭窗口")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyDialog.__set_properties
        self.SetTitle(u"运行算项及结果范围数值设置")
        self.text_ctrl_6.SetMinSize((80, 22))
        self.text_ctrl_7.SetMinSize((80, 22))
        self.text_ctrl_8.SetMinSize((80, 22))
        self.text_ctrl_9.SetMinSize((80, 22))
        self.text_ctrl_10.SetMinSize((80, 22))
        self.text_ctrl_11.SetMinSize((80, 22))
        self.text_ctrl_12.SetMinSize((80, 22))
        self.text_ctrl_13.SetMinSize((80, 22))
        self.text_ctrl_14.SetMinSize((80, 22))
        self.text_ctrl_15.SetMinSize((80, 22))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyDialog.__do_layout
        sizer_15 = wx.BoxSizer(wx.VERTICAL)
        sizer_16 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"算数项及结果取值范围"), wx.VERTICAL)
        sizer_30 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_21 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_20 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_19 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_18 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_17 = wx.BoxSizer(wx.HORIZONTAL)
        label_6 = wx.StaticText(self, wx.ID_ANY, u"何为算数项和结果？例如：3+7=10，3和7是算数项，10为结果。")
        sizer_15.Add(label_6, 0, wx.ALL | wx.EXPAND, 5)
        label_7 = wx.StaticText(self, wx.ID_ANY, u"第1个算数项取值范围：")
        sizer_17.Add(label_7, 0, 0, 0)
        sizer_17.Add(self.text_ctrl_6, 0, 0, 0)
        label_8 = wx.StaticText(self, wx.ID_ANY, u"到")
        sizer_17.Add(label_8, 0, 0, 0)
        sizer_17.Add(self.text_ctrl_7, 0, 0, 0)
        sizer_16.Add(sizer_17, 1, wx.EXPAND, 0)
        label_9 = wx.StaticText(self, wx.ID_ANY, u"第2个算数项取值范围：")
        sizer_18.Add(label_9, 0, 0, 0)
        sizer_18.Add(self.text_ctrl_8, 0, 0, 0)
        label_10 = wx.StaticText(self, wx.ID_ANY, u"到")
        sizer_18.Add(label_10, 0, 0, 0)
        sizer_18.Add(self.text_ctrl_9, 0, 0, 0)
        sizer_16.Add(sizer_18, 1, wx.EXPAND, 0)
        label_11 = wx.StaticText(self, wx.ID_ANY, u"第3个算数项取值范围：")
        sizer_19.Add(label_11, 0, 0, 0)
        sizer_19.Add(self.text_ctrl_10, 0, 0, 0)
        label_12 = wx.StaticText(self, wx.ID_ANY, u"到")
        sizer_19.Add(label_12, 0, 0, 0)
        sizer_19.Add(self.text_ctrl_11, 0, 0, 0)
        sizer_16.Add(sizer_19, 1, wx.EXPAND, 0)
        label_13 = wx.StaticText(self, wx.ID_ANY, u"第4个算数项取值范围：")
        sizer_20.Add(label_13, 0, 0, 0)
        sizer_20.Add(self.text_ctrl_12, 0, 0, 0)
        label_14 = wx.StaticText(self, wx.ID_ANY, u"到")
        sizer_20.Add(label_14, 0, 0, 0)
        sizer_20.Add(self.text_ctrl_13, 0, 0, 0)
        sizer_16.Add(sizer_20, 1, wx.EXPAND, 0)
        label_15 = wx.StaticText(self, wx.ID_ANY, u"运算结果取值范围：")
        sizer_21.Add(label_15, 0, 0, 0)
        sizer_21.Add(self.text_ctrl_14, 0, 0, 0)
        label_16 = wx.StaticText(self, wx.ID_ANY, u"到")
        sizer_21.Add(label_16, 0, 0, 0)
        sizer_21.Add(self.text_ctrl_15, 0, 0, 0)
        sizer_16.Add(sizer_21, 1, wx.EXPAND, 0)
        sizer_30.Add(self.button_9, 0, wx.ALIGN_CENTER, 0)
        sizer_30.Add(self.button_10, 0, wx.ALIGN_CENTER, 0)
        sizer_16.Add(sizer_30, 1, wx.ALIGN_CENTER | wx.SHAPED, 0)
        sizer_15.Add(sizer_16, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_15)
        sizer_15.Fit(self)
        self.Layout()
        # end wxGlade

# end of class MyDialog

class MyDialog1(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyDialog1.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.checkbox_2 = wx.CheckBox(self, wx.ID_ANY, u"+(加法)")
        self.checkbox_3 = wx.CheckBox(self, wx.ID_ANY, u"-(减法)")
        self.checkbox_4 = wx.CheckBox(self, wx.ID_ANY, u"×(乘法)")
        self.checkbox_5 = wx.CheckBox(self, wx.ID_ANY, u"÷(除法)")
        self.checkbox_6 = wx.CheckBox(self, wx.ID_ANY, u"+(加法)")
        self.checkbox_7 = wx.CheckBox(self, wx.ID_ANY, u"-(减法)")
        self.checkbox_8 = wx.CheckBox(self, wx.ID_ANY, u"×(乘法)")
        self.checkbox_9 = wx.CheckBox(self, wx.ID_ANY, u"÷(除法)")
        self.checkbox_10 = wx.CheckBox(self, wx.ID_ANY, u"+(加法)")
        self.checkbox_11 = wx.CheckBox(self, wx.ID_ANY, u"-(减法)")
        self.checkbox_12 = wx.CheckBox(self, wx.ID_ANY, u"×(乘法)")
        self.checkbox_13 = wx.CheckBox(self, wx.ID_ANY, u"÷(除法)")
        self.button_9 = wx.Button(self, wx.ID_ANY, u"提交修改")
        self.button_10 = wx.Button(self, wx.ID_ANY, u"关闭窗口")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyDialog1.__set_properties
        self.SetTitle("dialog_1")
        self.checkbox_2.SetValue(1)
        self.checkbox_7.SetValue(1)
        self.checkbox_10.SetValue(1)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyDialog1.__do_layout
        sizer_25 = wx.BoxSizer(wx.VERTICAL)
        sizer_26 = wx.BoxSizer(wx.VERTICAL)
        sizer_30 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_29 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"第一处运算符号选择"), wx.HORIZONTAL)
        sizer_28 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"第一处运算符号选择"), wx.HORIZONTAL)
        sizer_27 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"第一处运算符号选择"), wx.HORIZONTAL)
        label_18 = wx.StaticText(self, wx.ID_ANY, u"此处为多步运算题生成运算符号选择，比如4+8-5=，\n你要做的是选择+和-号位置可以使用什么运算符号。")
        sizer_25.Add(label_18, 0, wx.ALL | wx.EXPAND, 5)
        sizer_27.Add(self.checkbox_2, 0, 0, 0)
        sizer_27.Add(self.checkbox_3, 0, 0, 0)
        sizer_27.Add(self.checkbox_4, 0, 0, 0)
        sizer_27.Add(self.checkbox_5, 0, 0, 0)
        sizer_26.Add(sizer_27, 1, wx.EXPAND, 0)
        sizer_28.Add(self.checkbox_6, 0, 0, 0)
        sizer_28.Add(self.checkbox_7, 0, 0, 0)
        sizer_28.Add(self.checkbox_8, 0, 0, 0)
        sizer_28.Add(self.checkbox_9, 0, 0, 0)
        sizer_26.Add(sizer_28, 1, wx.EXPAND, 0)
        sizer_29.Add(self.checkbox_10, 0, 0, 0)
        sizer_29.Add(self.checkbox_11, 0, 0, 0)
        sizer_29.Add(self.checkbox_12, 0, 0, 0)
        sizer_29.Add(self.checkbox_13, 0, 0, 0)
        sizer_26.Add(sizer_29, 1, wx.EXPAND, 0)
        sizer_30.Add(self.button_9, 0, wx.ALIGN_CENTER, 0)
        sizer_30.Add(self.button_10, 0, wx.ALIGN_CENTER, 0)
        sizer_26.Add(sizer_30, 1, wx.ALIGN_CENTER, 0)
        sizer_25.Add(sizer_26, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_25)
        sizer_25.Fit(self)
        self.Layout()
        # end wxGlade

# end of class MyDialog1

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
