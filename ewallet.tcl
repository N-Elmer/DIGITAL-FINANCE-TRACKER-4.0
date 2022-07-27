#############################################################################
# Generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#  Feb 02, 2021 05:43:35 PM WAT  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    tk_messageBox -title Error -message  "You must open project files from within PAGE."
    exit}


set image_list { \
    image22 "../../../../../../page/rupixen-com-Q59HmzK38eQ-unsplash.jpg" \
}
vTcl:create_project_images $image_list   ;# In image.tcl


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_font_dft_desc)  TkDefaultFont
set vTcl(actual_gui_font_dft_name)  TkDefaultFont
set vTcl(actual_gui_font_text_desc)  TkTextFont
set vTcl(actual_gui_font_text_name)  TkTextFont
set vTcl(actual_gui_font_fixed_desc)  TkFixedFont
set vTcl(actual_gui_font_fixed_name)  TkFixedFont
set vTcl(actual_gui_font_menu_desc)  TkMenuFont
set vTcl(actual_gui_font_menu_name)  TkMenuFont
set vTcl(actual_gui_font_tooltip_desc)  TkDefaultFont
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top45 {base} {
    global vTcl
    if {$base == ""} {
        set base .top45
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 1195x604+0+9
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1366 764
    wm minsize $top 1000 500
    wm overrideredirect $top 0
    wm resizable $top 0 0
    wm deiconify $top
    wm title $top "ELECTRONIC WALLET"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    vTcl:copy_lock $top
    ttk::style configure TNotebook -background $vTcl(actual_gui_bg)
    ttk::style configure TNotebook.Tab -background $vTcl(actual_gui_bg)
    ttk::style configure TNotebook.Tab -foreground $vTcl(actual_gui_fg)
    ttk::style configure TNotebook.Tab -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style map TNotebook.Tab -background [list disabled $vTcl(actual_gui_bg) selected $vTcl(complement_color)]
    ttk::notebook $top.tNo47 \
        -width 1156 -height 626 -takefocus {} 
    vTcl:DefineAlias "$top.tNo47" "TNotebook1" vTcl:WidgetProc "Toplevel1" 1
    frame $top.tNo47.t1 \
        -background #ffffff -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black 
    vTcl:DefineAlias "$top.tNo47.t1" "TNotebook1_t2_1_1" vTcl:WidgetProc "Toplevel1" 1
    $top.tNo47 add $top.tNo47.t1 \
        -padding 0 -sticky nsew -state normal -text MANAGE -image {} \
        -compound left -underline -1 
    set site_4_0  $top.tNo47.t1
    ttk::style configure TPanedwindow -background $vTcl(actual_gui_bg)
    ttk::style configure TPanedwindow.Label -background $vTcl(actual_gui_bg)
    ttk::style configure TPanedwindow.Label -foreground $vTcl(actual_gui_fg)
    ttk::style configure TPanedwindow.Label -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::panedwindow $site_4_0.tPa51 \
        -orient horizontal 
    vTcl:DefineAlias "$site_4_0.tPa51" "TPanedwindow1" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure TLabelframe.Label -background $vTcl(actual_gui_bg)
    ttk::style configure TLabelframe.Label -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabelframe.Label -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style configure TLabelframe -background $vTcl(actual_gui_bg)
    ttk::labelframe $site_4_0.tPa51.p1 \
        -text DATA -relief groove -width 75 -height 200 
    vTcl:DefineAlias "$site_4_0.tPa51.p1" "TPanedwindow1_p1" vTcl:WidgetProc "Toplevel1" 1
    set site_6_0 $site_4_0.tPa51.p1
    label $site_6_0.lab45 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background #607D8B -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -relief groove -text DATE 
    vTcl:DefineAlias "$site_6_0.lab45" "Label1" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_6_0.lab45
    entry $site_6_0.ent46 \
        -background white -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -textvariable DateEntryVar -width 224 
    vTcl:DefineAlias "$site_6_0.ent46" "DateEntry" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_6_0.ent46
    label $site_6_0.lab47 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background #607D8B -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -relief groove -text INCOME 
    vTcl:DefineAlias "$site_6_0.lab47" "Label1_1" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_6_0.lab47
    entry $site_6_0.ent48 \
        -background white -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground #ffffff -textvariable IncomeEntryVar -width 224 
    vTcl:DefineAlias "$site_6_0.ent48" "IncomeEntry" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_6_0.ent48
    label $site_6_0.lab49 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background #607D8B -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -relief groove -text {INCOME REMARKS} 
    vTcl:DefineAlias "$site_6_0.lab49" "Label1_1_1" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_6_0.lab49
    entry $site_6_0.ent50 \
        -background white -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -textvariable IncomeRemarksEntryVar \
        -width 224 
    vTcl:DefineAlias "$site_6_0.ent50" "IncomeRemarksEntry" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_6_0.ent50
    label $site_6_0.lab51 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background #607D8B -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -relief groove -text EXPENDITURE 
    vTcl:DefineAlias "$site_6_0.lab51" "Label1_1_1_1" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_6_0.lab51
    entry $site_6_0.ent52 \
        -background white -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -textvariable ExpenditureEntryVar -width 224 
    vTcl:DefineAlias "$site_6_0.ent52" "ExpenditureEntry" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_6_0.ent52
    label $site_6_0.lab53 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background #607D8B -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -relief groove -text {EXPENDITURE REMARKS} 
    vTcl:DefineAlias "$site_6_0.lab53" "Label1_1_1_1_1" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_6_0.lab53
    entry $site_6_0.ent54 \
        -background white -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -textvariable ExpenditureRemarksEntryVar \
        -width 224 
    vTcl:DefineAlias "$site_6_0.ent54" "ExpenditureRemarksEntry" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_6_0.ent54
    button $site_6_0.but55 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #00ff40 -command SubmitButtonCommand \
        -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) -highlightbackground #ffffff \
        -highlightcolor #ffffff -pady 0 -state normal -text SUBMIT 
    vTcl:DefineAlias "$site_6_0.but55" "SubmitButton" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_6_0.but55
    button $site_6_0.but57 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #ff0000 -command DeleteButtonCommand \
        -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground #ffffff -highlightbackground #ffffff \
        -highlightcolor #ffffff -pady 0 -text DELETE 
    vTcl:DefineAlias "$site_6_0.but57" "DeleteButton" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_6_0.but57
    button $site_6_0.but58 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #808080 -command ClearButtonCommand \
        -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) -highlightbackground #ffffff \
        -highlightcolor #ffffff -pady 0 -text CLEAR 
    vTcl:DefineAlias "$site_6_0.but58" "ClearButton" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_6_0.but58
    button $site_6_0.but59 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #0080c0 -command AnalyticsButtonCommand \
        -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground #ffffff -highlightbackground #ffffff \
        -highlightcolor #ffffff -pady 0 -text ANALYTICS 
    vTcl:DefineAlias "$site_6_0.but59" "AnalyticsButton" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_6_0.but59
    place $site_6_0.lab45 \
        -in $site_6_0 -x 0 -relx 0.041 -y 0 -rely 0.051 -width 0 \
        -relwidth 0.22 -height 0 -relheight 0.053 -anchor nw \
        -bordermode ignore 
    place $site_6_0.ent46 \
        -in $site_6_0 -x 0 -relx 0.041 -y 0 -rely 0.102 -width 224 \
        -relwidth 0 -height 30 -relheight 0 -anchor nw -bordermode ignore 
    place $site_6_0.lab47 \
        -in $site_6_0 -x 0 -relx 0.041 -y 0 -rely 0.186 -width 0 \
        -relwidth 0.302 -height 0 -relheight 0.051 -anchor nw \
        -bordermode ignore 
    place $site_6_0.ent48 \
        -in $site_6_0 -x 0 -relx 0.041 -y 0 -rely 0.237 -width 224 \
        -relwidth 0 -height 30 -relheight 0 -anchor nw -bordermode ignore 
    place $site_6_0.lab49 \
        -in $site_6_0 -x 0 -relx 0.041 -y 0 -rely 0.322 -width 0 \
        -relwidth 0.629 -height 0 -relheight 0.051 -anchor nw \
        -bordermode ignore 
    place $site_6_0.ent50 \
        -in $site_6_0 -x 0 -relx 0.041 -y 0 -rely 0.373 -width 224 \
        -relwidth 0 -height 30 -relheight 0 -anchor nw -bordermode ignore 
    place $site_6_0.lab51 \
        -in $site_6_0 -x 0 -relx 0.041 -y 0 -rely 0.458 -width 0 \
        -relwidth 0.506 -height 0 -relheight 0.051 -anchor nw \
        -bordermode ignore 
    place $site_6_0.ent52 \
        -in $site_6_0 -x 0 -relx 0.041 -y 0 -rely 0.508 -width 224 \
        -relwidth 0 -height 30 -relheight 0 -anchor nw -bordermode ignore 
    place $site_6_0.lab53 \
        -in $site_6_0 -x 0 -relx 0.041 -y 0 -rely 0.593 -width 0 \
        -relwidth 0.792 -height 0 -relheight 0.051 -anchor nw \
        -bordermode ignore 
    place $site_6_0.ent54 \
        -in $site_6_0 -x 0 -relx 0.041 -y 0 -rely 0.645 -width 224 \
        -relwidth 0 -height 30 -relheight 0 -anchor nw -bordermode ignore 
    place $site_6_0.but55 \
        -in $site_6_0 -x 0 -relx 0.041 -y 0 -rely 0.711 -width 97 -relwidth 0 \
        -height 44 -relheight 0 -anchor nw -bordermode ignore 
    place $site_6_0.but57 \
        -in $site_6_0 -x 0 -relx 0.571 -y 0 -rely 0.711 -width 94 -relwidth 0 \
        -height 44 -relheight 0 -anchor nw -bordermode ignore 
    place $site_6_0.but58 \
        -in $site_6_0 -x 0 -relx 0.041 -y 0 -rely 0.812 -width 224 \
        -relwidth 0 -height 44 -relheight 0 -anchor nw -bordermode ignore 
    place $site_6_0.but59 \
        -in $site_6_0 -x 0 -relx 0.041 -y 0 -rely 0.897 -width 224 \
        -relwidth 0 -height 44 -relheight 0 -anchor nw -bordermode ignore 
    $site_4_0.tPa51 add $site_4_0.tPa51.p1 
    $site_4_0.tPa51 pane $site_4_0.tPa51.p1 -weight 0
    ttk::style configure TLabelframe.Label -background $vTcl(actual_gui_bg)
    ttk::style configure TLabelframe.Label -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabelframe.Label -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style configure TLabelframe -background $vTcl(actual_gui_bg)
    ttk::labelframe $site_4_0.tPa51.p2 \
        -text TRANSACTION -relief groove -width 125 -height 200 
    vTcl:DefineAlias "$site_4_0.tPa51.p2" "TPanedwindow1_p2" vTcl:WidgetProc "Toplevel1" 1
    set site_6_1 $site_4_0.tPa51.p2
    ttk::style configure Treeview \
         -font  "$vTcl(actual_gui_font_treeview_desc)"
    vTcl::widgets::ttk::scrolledtreeview::CreateCmd $site_6_1.scr48 \
        -relief groove -background $vTcl(actual_gui_bg) -height 437 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 690 
    vTcl:DefineAlias "$site_6_1.scr48" "Database" vTcl:WidgetProc "Toplevel1" 1

    .top45.tNo47.t1.tPa51.p2.scr48.01 configure -columns "Col1 Col2 Col3 Col4 Col5 Col6" \
        -height 4
        .top45.tNo47.t1.tPa51.p2.scr48.01 configure -columns {Col1 Col2 Col3 Col4 Col5 Col6}
        .top45.tNo47.t1.tPa51.p2.scr48.01 heading #0 -text {Tree}
        .top45.tNo47.t1.tPa51.p2.scr48.01 heading #0 -anchor center
        .top45.tNo47.t1.tPa51.p2.scr48.01 column #0 -width 0
        .top45.tNo47.t1.tPa51.p2.scr48.01 column #0 -minwidth 0
        .top45.tNo47.t1.tPa51.p2.scr48.01 column #0 -stretch 0
        .top45.tNo47.t1.tPa51.p2.scr48.01 column #0 -anchor center
        .top45.tNo47.t1.tPa51.p2.scr48.01 heading Col1 -text {ID}
        .top45.tNo47.t1.tPa51.p2.scr48.01 heading Col1 -anchor center
        .top45.tNo47.t1.tPa51.p2.scr48.01 column Col1 -width 76
        .top45.tNo47.t1.tPa51.p2.scr48.01 column Col1 -minwidth 76
        .top45.tNo47.t1.tPa51.p2.scr48.01 column Col1 -stretch 0
        .top45.tNo47.t1.tPa51.p2.scr48.01 column Col1 -anchor center
        .top45.tNo47.t1.tPa51.p2.scr48.01 heading Col2 -text {DATE}
        .top45.tNo47.t1.tPa51.p2.scr48.01 heading Col2 -anchor center
        .top45.tNo47.t1.tPa51.p2.scr48.01 column Col2 -width 93
        .top45.tNo47.t1.tPa51.p2.scr48.01 column Col2 -minwidth 93
        .top45.tNo47.t1.tPa51.p2.scr48.01 column Col2 -stretch 0
        .top45.tNo47.t1.tPa51.p2.scr48.01 column Col2 -anchor center
        .top45.tNo47.t1.tPa51.p2.scr48.01 heading Col3 -text {INCOME}
        .top45.tNo47.t1.tPa51.p2.scr48.01 heading Col3 -anchor center
        .top45.tNo47.t1.tPa51.p2.scr48.01 column Col3 -width 95
        .top45.tNo47.t1.tPa51.p2.scr48.01 column Col3 -minwidth 95
        .top45.tNo47.t1.tPa51.p2.scr48.01 column Col3 -stretch 0
        .top45.tNo47.t1.tPa51.p2.scr48.01 column Col3 -anchor center
        .top45.tNo47.t1.tPa51.p2.scr48.01 heading Col4 -text {INCOME REMARKS}
        .top45.tNo47.t1.tPa51.p2.scr48.01 heading Col4 -anchor center
        .top45.tNo47.t1.tPa51.p2.scr48.01 column Col4 -width 156
        .top45.tNo47.t1.tPa51.p2.scr48.01 column Col4 -minwidth 156
        .top45.tNo47.t1.tPa51.p2.scr48.01 column Col4 -stretch 0
        .top45.tNo47.t1.tPa51.p2.scr48.01 column Col4 -anchor center
        .top45.tNo47.t1.tPa51.p2.scr48.01 heading Col5 -text {EXPENDITURE}
        .top45.tNo47.t1.tPa51.p2.scr48.01 heading Col5 -anchor center
        .top45.tNo47.t1.tPa51.p2.scr48.01 column Col5 -width 95
        .top45.tNo47.t1.tPa51.p2.scr48.01 column Col5 -minwidth 95
        .top45.tNo47.t1.tPa51.p2.scr48.01 column Col5 -stretch 0
        .top45.tNo47.t1.tPa51.p2.scr48.01 column Col5 -anchor center
        .top45.tNo47.t1.tPa51.p2.scr48.01 heading Col6 -text {EXPENDITURE REMARKS}
        .top45.tNo47.t1.tPa51.p2.scr48.01 heading Col6 -anchor center
        .top45.tNo47.t1.tPa51.p2.scr48.01 column Col6 -width 158
        .top45.tNo47.t1.tPa51.p2.scr48.01 column Col6 -minwidth 158
        .top45.tNo47.t1.tPa51.p2.scr48.01 column Col6 -stretch 0
        .top45.tNo47.t1.tPa51.p2.scr48.01 column Col6 -anchor center
    vTcl:copy_lock $site_6_1.scr48
    label $site_6_1.lab69 \
        -activebackground #f9f9f9 -activeforeground black -background #0080ff \
        -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 20 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {ELECTRONIC WALLET} 
    vTcl:DefineAlias "$site_6_1.lab69" "Label3_1" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_6_1.lab69
    place $site_6_1.scr48 \
        -in $site_6_1 -x 0 -relx 0.014 -y 0 -rely 0.237 -width 0 \
        -relwidth 0.967 -height 0 -relheight 0.739 -anchor nw \
        -bordermode ignore 
    place $site_6_1.lab69 \
        -in $site_6_1 -x 0 -relx 0.014 -y 0 -rely 0.068 -width 0 \
        -relwidth 0.956 -height 0 -relheight 0.137 -anchor nw \
        -bordermode ignore 
    $site_4_0.tPa51 add $site_4_0.tPa51.p2 
    $site_4_0.tPa51 pane $site_4_0.tPa51.p2 -weight 0
    bind .top45.tNo47.t1.tPa51 <Map> {
        .top45.tNo47.t1.tPa51 sashpos 0 245
        bind .top45.tNo47.t1.tPa51 <Map> {}
    }
    vTcl:copy_lock $site_4_0.tPa51
    ttk::style configure TPanedwindow -background $vTcl(actual_gui_bg)
    ttk::style configure TPanedwindow.Label -background $vTcl(actual_gui_bg)
    ttk::style configure TPanedwindow.Label -foreground $vTcl(actual_gui_fg)
    ttk::style configure TPanedwindow.Label -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::panedwindow $site_4_0.tPa52
    vTcl:DefineAlias "$site_4_0.tPa52" "TPanedwindow2" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure TLabelframe.Label -background $vTcl(actual_gui_bg)
    ttk::style configure TLabelframe.Label -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabelframe.Label -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style configure TLabelframe -background $vTcl(actual_gui_bg)
    ttk::labelframe $site_4_0.tPa52.p1 \
        -text COMPARE -relief groove -width 200 -height 150 
    vTcl:DefineAlias "$site_4_0.tPa52.p1" "TPanedwindow2_p1" vTcl:WidgetProc "Toplevel1" 1
    set site_6_0 $site_4_0.tPa52.p1
    entry $site_6_0.ent57 \
        -background white -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -state readonly \
        -textvariable ExpenditureDisplayEntryVar -width 194 
    vTcl:DefineAlias "$site_6_0.ent57" "ExpenditureDisplayEntry" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_6_0.ent57
    entry $site_6_0.ent61 \
        -background white -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -state readonly \
        -textvariable IncomeDisplayEntryVar -width 194 
    vTcl:DefineAlias "$site_6_0.ent61" "IncomeDisplayEntry" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_6_0.ent61
    button $site_6_0.but62 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #00ff40 -command IncomeSumButtonCommand \
        -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) -highlightbackground #ffffff \
        -highlightcolor #ffffff -pady 0 -text {GET TOTAL INCOME} 
    vTcl:DefineAlias "$site_6_0.but62" "IncomeSumButton" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_6_0.but62
    button $site_6_0.but65 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #ff0000 -command ExpenditureSumButtonCommand \
        -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) -highlightbackground #ffffff \
        -highlightcolor #ffffff -image image22 -pady 0 \
        -text {GET TOTAL EXPENDITURE} 
    vTcl:DefineAlias "$site_6_0.but65" "ExpenditureSumButton" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_6_0.but65
    place $site_6_0.ent57 \
        -in $site_6_0 -x 0 -relx 0.082 -y 0 -rely 0.696 -width 194 \
        -relwidth 0 -height 100 -relheight 0 -anchor nw -bordermode ignore 
    place $site_6_0.ent61 \
        -in $site_6_0 -x 0 -relx 0.082 -y 0 -rely 0.232 -width 194 \
        -relwidth 0 -height 100 -relheight 0 -anchor nw -bordermode ignore 
    place $site_6_0.but62 \
        -in $site_6_0 -x 0 -relx 0.082 -y 0 -rely 0.087 -width 197 \
        -relwidth 0 -height 34 -relheight 0 -anchor nw -bordermode ignore 
    place $site_6_0.but65 \
        -in $site_6_0 -x 0 -relx 0.082 -y 0 -rely 0.551 -width 197 \
        -relwidth 0 -height 34 -relheight 0 -anchor nw -bordermode ignore 
    $site_4_0.tPa52 add $site_4_0.tPa52.p1 
    $site_4_0.tPa52 pane $site_4_0.tPa52.p1 -weight 0
    ttk::style configure TLabelframe.Label -background $vTcl(actual_gui_bg)
    ttk::style configure TLabelframe.Label -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabelframe.Label -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style configure TLabelframe -background $vTcl(actual_gui_bg)
    ttk::labelframe $site_4_0.tPa52.p2 \
        -text BALANCE -relief groove -width 200 -height 50 
    vTcl:DefineAlias "$site_4_0.tPa52.p2" "TPanedwindow2_p2" vTcl:WidgetProc "Toplevel1" 1
    set site_6_1 $site_4_0.tPa52.p2
    entry $site_6_1.ent58 \
        -background white -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -state readonly \
        -textvariable BalanceDisplayEntryVar -width 194 
    vTcl:DefineAlias "$site_6_1.ent58" "BalanceDisplayEntry" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_6_1.ent58
    button $site_6_1.but64 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #0080c0 -command BalanceButtonCommand \
        -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) -highlightbackground #ffffff \
        -highlightcolor #ffffff -pady 0 -text {GET FINAL BALANCE} 
    vTcl:DefineAlias "$site_6_1.but64" "BalanceButton" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_6_1.but64
    place $site_6_1.ent58 \
        -in $site_6_1 -x 0 -relx 0.082 -y 0 -rely 0.366 -width 194 \
        -relwidth 0 -height 100 -relheight 0 -anchor nw -bordermode ignore 
    place $site_6_1.but64 \
        -in $site_6_1 -x 0 -relx 0.082 -y 0 -rely 0.163 -width 197 \
        -relwidth 0 -height 34 -relheight 0 -anchor nw -bordermode ignore 
    $site_4_0.tPa52 add $site_4_0.tPa52.p2 
    $site_4_0.tPa52 pane $site_4_0.tPa52.p2 -weight 0
    bind .top45.tNo47.t1.tPa52 <Map> {
        .top45.tNo47.t1.tPa52 sashpos 0 345
        bind .top45.tNo47.t1.tPa52 <Map> {}
    }
    vTcl:copy_lock $site_4_0.tPa52
    place $site_4_0.tPa51 \
        -in $site_4_0 -x 0 -y 0 -width 0 -relwidth 0.798 -height 0 \
        -relheight 0.998 -anchor nw -bordermode ignore 
    place $site_4_0.tPa52 \
        -in $site_4_0 -x 0 -relx 0.803 -y 0 -width 0 -relwidth 0.203 \
        -height 0 -relheight 1.007 -anchor nw -bordermode ignore 
    vTcl:copy_lock $top.tNo47
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.tNo47 \
        -in $top -x 0 -y 0 -width 0 -relwidth 1.004 -height 0 \
        -relheight 1.023 -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top45 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

