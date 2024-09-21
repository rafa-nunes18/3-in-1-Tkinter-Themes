# Copyright (c) 2021 rdbende <rdbende@gmail.com>

# The Sun-Valley theme is a beautiful and modern ttk theme.

package require Tk 8.6

namespace eval ttk::theme::sun-valley-dark {

  variable version 2.5
  package provide ttk::theme::sun-valley-dark $version
  variable colors
  array set colors {
    -fg             "#fafafa"
    -bg             "#1c1c1c"
    -disabledfg     "#595959"
    -disabledbg     "#ffffff" 
    -selectfg       "#ffffff"
    -selectbg       "#2f60d8"
    -accent         "#57c8ff"
  }

  proc LoadImages {imgdir} {
    variable I
    foreach file [glob -directory $imgdir *.png] {
      set img [file tail [file rootname $file]]
      set I($img) [image create photo -file $file -format png]
    }
  }

  LoadImages [file join [file dirname [info script]] sun-dark]

  # Settings
  ttk::style theme create sun-valley-dark -parent default -settings {
    ttk::style configure . \
      -background $colors(-bg) \
      -foreground $colors(-fg) \
      -troughcolor $colors(-bg) \
      -focuscolor $colors(-selectbg) \
      -selectbackground $colors(-selectbg) \
      -selectforeground $colors(-selectfg) \
      -insertwidth 1 \
      -insertcolor $colors(-fg) \
      -fieldbackground $colors(-selectbg) \
      -font {SunValleyBodyFont 10} \
      -borderwidth 1 \
      -relief flat
    
    ttk::style map . -foreground [list disabled $colors(-disabledfg)]

    tk_setPalette background [ttk::style lookup . -background] \
      foreground [ttk::style lookup . -foreground] \
      highlightColor [ttk::style lookup . -focuscolor] \
      selectBackground [ttk::style lookup . -selectbackground] \
      selectForeground [ttk::style lookup . -selectforeground] \
      activeBackground [ttk::style lookup . -selectbackground] \
      activeForeground [ttk::style lookup . -selectforeground]

    option add *font [ttk::style lookup . -font]    

    # Button
    ttk::style layout TButton {
      TButton.button -children {
        TButton.padding -children {
          TButton.label -side left -expand 1
        } 
      }
    }

    ttk::style configure TButton -padding {8 2 8 3} -anchor center -foreground $colors(-fg)
    ttk::style map TButton -foreground [list disabled "#7a7a7a" pressed "#d0d0d0"]
    
    ttk::style element create TButton.button image \
      [list $I(button-rest) \
        {selected disabled} $I(button-dis) \
        disabled $I(button-dis) \
        selected $I(button-rest) \
        pressed $I(button-pressed) \
        {active focus} $I(button-focus-hover) \
        active $I(button-focus) \
        focus $I(button-rest) \
      ] -border 4 -sticky nsew
      
    # RedButton 
    ttk::style layout Redbutton.TButton {
       Redbutton.TButton.button -children {
         Redbutton.TButton.padding -children {
           Redbutton.TButton.label -side left -expand 1
        } 
      }
    }

    ttk::style configure Redbutton.TButton -padding {8 2 8 3} -anchor center -foreground $colors(-fg)
    ttk::style map Redbutton.TButton -foreground \
      [list disabled "#a2a2a2"\
       pressed "Black" \
       active "White" \
      ]
    
    ttk::style element create Redbutton.TButton.button image \
      [list $I(button-rest2) \
        {selected disabled} $I(button-dis) \
        disabled $I(button-dis) \
        selected $I(button-rest) \
        pressed $I(button-pressed) \
        {active focus} $I(button-focus-hover) \
        active $I(botao-x) \
        focus $I(button-focus) \
      ] -border 4 -sticky nsew

    # RedButton_linux 
    ttk::style layout Redbuttonlinux.TButton {
       Redbuttonlinux.TButton.button -children {
         Redbuttonlinux.TButton.padding -children {
           Redbuttonlinux.TButton.label -side left -expand 1
        } 
      }
    }

    ttk::style configure Redbuttonlinux.TButton -padding {8 2 8 3} -anchor center -foreground $colors(-fg)
    ttk::style map Redbuttonlinux.TButton -foreground \
      [list disabled "#a2a2a2"\
       pressed "Black" \
       active "White" \
      ]
    
    ttk::style element create Redbuttonlinux.TButton.button image \
      [list $I(button-rest) \
        {selected disabled} $I(button-dis) \
        disabled $I(button-dis) \
        selected $I(button-rest) \
        pressed $I(button-pressed) \
        {active focus} $I(button-focus-hover) \
        active $I(botao-x-linux) \
        focus $I(button-rest) \
      ] -border 4 -sticky nsew

    # XButton
    ttk::style layout XButton.TButton {
       XButton.TButton.button -children {
         XButton.TButton.padding -children {
           XButton.TButton.label -side left -expand 1
        } 
      }
    }

    ttk::style configure XButton.TButton -padding {8 2 8 3} -anchor center -foreground $colors(-fg)
    ttk::style map XButton.TButton -foreground \
      [list disabled "#a2a2a2"\
       pressed "Black" \
       active "White" \
      ]
    
    ttk::style element create XButton.TButton.button image \
      [list $I(button-rest2) \
        {selected disabled} $I(button-dis) \
        disabled $I(button-dis) \
        selected $I(button-rest) \
        pressed $I(button-pressed) \
        {active focus} $I(button-focus-hover) \
        active $I(botao-x) \
        focus $I(button-focus) \
      ] -border 4 -sticky nsew

    # Toolbutton
    ttk::style layout Toolbutton {
      Toolbutton.button -children {
        Toolbutton.padding -children {
          Toolbutton.label -side left -expand 1
        } 
      }
    }    

    ttk::style configure Toolbutton -padding {8 4 8 4} -anchor center
    
    ttk::style element create Toolbutton.button image \
      [list $I(empty) \
        disabled $I(button-dis) \
        pressed $I(button-pressed) \
        {active focus} $I(button-focus-hover) \
        active $I(button-focus) \
        focus $I(button-focus) \
      ] -border 4 -sticky nsew

    # Accent.TButton
    ttk::style layout Accent.TButton {
      Accent.TButton.button -children {
        Accent.TButton.padding -children {
          Accent.TButton.label -side left -expand 1
        } 
      }
    }

    ttk::style configure Accent.TButton -padding {8 4 8 4} -anchor center -foreground "#000000"
    ttk::style map Accent.TButton -foreground [list pressed "#25536a" disabled "#a5a5a5"]

    ttk::style element create Accent.TButton.button image \
      [list $I(button-accent-rest) \
        {selected disabled} $I(button-accent-dis) \
        disabled $I(button-accent-dis) \
        selected $I(button-accent-rest) \
        pressed $I(button-accent-pressed) \
        {active focus} $I(button-accent-focus-hover) \
        active $I(button-accent-hover) \
        focus $I(button-accent-focus) \
      ] -border 4 -sticky nsew

    # Menubutton
    ttk::style layout TMenubutton {
      Menubutton.button -children {
        Menubutton.padding -children {
          Menubutton.label -side left -expand 1
          Menubutton.indicator -side right -sticky nsew
        }
      }
    }

    ttk::style configure TMenubutton -padding {8 4 4 4}

    ttk::style element create Menubutton.button image \
      [list $I(button-rest) \
        disabled $I(button-dis) \
        pressed $I(button-pressed) \
        {active focus} $I(button-focus-hover) \
        active $I(button-focus) \
        focus $I(button-focus) \
      ] -border 4 -sticky nsew 

    ttk::style element create Menubutton.indicator image $I(down) -width 10 -sticky e

    # OptionMenu
    ttk::style layout TOptionMenu {
      OptionMenu.button -children {
        OptionMenu.padding -children {
          OptionMenu.label -side left -expand 1
          OptionMenu.indicator -side right -sticky nsew
        }
      }
    }
    
    ttk::style configure TOptionMenu -padding {8 4 4 4}

    ttk::style element create OptionMenu.button image \
      [list $I(button-rest) \
        disabled $I(button-dis) \
        pressed $I(button-pressed) \
        {active focus} $I(button-focus-hover) \
        active $I(button-focus) \
        focus $I(button-focus) \
      ] -border 4 -sticky nsew 

    ttk::style element create OptionMenu.indicator image $I(down) -width 10 -sticky e

    # Checkbutton
    ttk::style layout TCheckbutton {
      Checkbutton.button -children {
        Checkbutton.padding -children {
          Checkbutton.indicator -side left
          Checkbutton.label -side right -expand 1
        }
      }
    }

    ttk::style configure TCheckbutton -padding 4

    ttk::style element create Checkbutton.indicator image \
      [list $I(check-unsel-rest) \
        {alternate disabled} $I(check-tri-dis) \
        {selected disabled} $I(check-dis) \
        disabled $I(check-unsel-dis) \
        {pressed alternate} $I(check-tri-hover) \
        {active focus alternate} $I(check-tri-focus-hover) \
        {active alternate} $I(check-tri-hover) \
        {focus alternate} $I(check-tri-focus) \
        alternate $I(check-tri-rest) \
        {pressed selected} $I(check-hover) \
        {active focus selected} $I(check-focus-hover) \
        {active selected} $I(check-hover) \
        {focus selected} $I(check-focus) \
        selected $I(check-rest) \
        {pressed !selected} $I(check-unsel-pressed) \
        {active focus} $I(check-unsel-focus-hover) \
        active $I(check-unsel-hover) \
        focus $I(check-unsel-focus) \
      ] -width 26 -sticky w

    # Switch.Checkbutton
    ttk::style layout Switch.Checkbutton {
      SSwitch.Checkbutton.button -children {
        Switch.Checkbutton.padding -children {
          Switch.Checkbutton.indicator -side left
          Switch.Checkbutton.label -side right -expand 1
        }
      }
    }
    
    ttk::style configure Switch.Checkbutton -padding {8 4 8 4} -width -10 -anchor center -foreground $colors(-fg)
   
    ttk::style map Switch.Checkbutton -foreground \
        [list {selected pressed} #ffffff \
        {active selected} #7a7a7a \
            selected  #57c8ff                 
        ]

    ttk::style element create Switch.Checkbutton.indicator image \
      [list $I(switch-off-rest) \
        {selected disabled} $I(switch-dis) \
        disabled $I(switch-off-dis) \
        {pressed selected} $I(switch-pressed) \
        {active focus selected} $I(switch-focus-hover) \
        {active selected} $I(switch-hover) \
        {focus selected} $I(switch-focus) \
        selected $I(switch-rest) \
        {pressed !selected} $I(switch-off-pressed) \
        {active focus} $I(switch-off-focus-hover) \
        active $I(switch-off-hover) \
        focus $I(switch-off-focus) \
      ] -width 46 -sticky w

    # Toggle.TButton
    ttk::style layout Toggle.TButton {
      Toggle.TButton.button -children {
        Toggle.TButton.padding -children {
          Toggle.TButton.label -side left -expand 1
        } 
      }
    }

    ttk::style configure Toggle.TButton -padding {8 4 8 4} -anchor center -foreground $colors(-fg)

    ttk::style map Toggle.TButton -foreground \
      [list {selected disabled} "#a5a5a5" \
        {selected pressed} "#d0d0d0" \
        selected "#000000" \
        pressed "#25536a" \
        disabled "#7a7a7a"
      ]

    ttk::style element create Toggle.TButton.button image \
      [list $I(button-rest) \
        {selected disabled} $I(button-accent-dis) \
        disabled $I(button-dis) \
        {pressed selected} $I(button-rest) \
        {active focus selected} $I(button-accent-focus-hover) \
        {active selected} $I(button-accent-hover) \
        {focus selected} $I(button-accent-focus) \
        selected $I(button-accent-rest) \
        {pressed !selected} $I(button-accent-rest) \
        {active focus} $I(button-focus-hover) \
        active $I(button-focus) \
        focus $I(button-focus) \
      ] -border 4 -sticky nsew

    # Radiobutton
    ttk::style layout TRadiobutton {
      Radiobutton.button -children {
        Radiobutton.padding -children {
          Radiobutton.indicator -side left
          Radiobutton.label -side right -expand 1
        }
      }
    }

    ttk::style configure TRadiobutton -padding 4

    ttk::style element create Radiobutton.indicator image \
      [list $I(radio-unsel-rest) \
        {selected disabled} $I(radio-dis) \
        disabled $I(radio-unsel-dis) \
        {pressed selected} $I(radio-pressed) \
        {active focus selected} $I(radio-focus-hover) \
        {active selected} $I(radio-hover) \
        {focus selected} $I(radio-focus) \
        selected $I(radio-rest) \
        {pressed !selected} $I(radio-unsel-pressed) \
        {active focus} $I(radio-unsel-focus-hover) \
        active $I(radio-unsel-hover) \
        focus $I(radio-unsel-focus) \
      ] -width 26 -sticky w

    # Entry
    ttk::style configure TEntry -foreground $colors(-fg) -padding {6 1 4 2}
    ttk::style map TEntry -foreground [list disabled "#757575" pressed "#cfcfcf"]

    ttk::style element create Entry.field image \
      [list $I(textbox-rest) \
        {focus hover !invalid} $I(textbox-focus) \
        invalid $I(textbox-error) \
        disabled $I(textbox-dis) \
        {focus !invalid} $I(textbox-focus) \
        hover $I(button-focus) \
      ] -border 5 -sticky nsew

    # Combobox
    ttk::style layout TCombobox {
      Combobox.field -sticky nsew -children {
        Combobox.arrow -side right -sticky ns
        Combobox.padding -sticky nsew -children {
          Combobox.textarea -sticky nsew
        }
      }
    }
        
    ttk::style configure TCombobox -foreground $colors(-fg) -padding {6 1 0 2}
    ttk::style configure ComboboxPopdownFrame -borderwidth 1 -relief solid
    ttk::style map TCombobox -foreground [list disabled "#757575" pressed "#cfcfcf"]
    
    ttk::style map TCombobox -selectbackground [list \
      {readonly hover} $colors(-selectbg) \
      {readonly focus} $colors(-selectbg) \
    ] -selectforeground [list \
      {readonly hover} $colors(-selectfg) \
      {readonly focus} $colors(-selectfg) \
    ]

    ttk::style element create Combobox.field image \
      [list $I(textbox-rest) \
          {readonly disabled} $I(button-dis) \
          {readonly pressed} $I(button-dis) \
          {readonly focus hover} $I(button-focus) \
          {readonly focus} $I(button-focus) \
          {readonly hover} $I(button-focus) \
          {focus hover} $I(box-accent) \
          readonly $I(button-dis) \
          invalid $I(textbox-error) \
          disabled $I(textbox-dis) \
          focus $I(textbox-focus) \
          hover $I(button-focus-hover) \
      ] -border 5 -padding {8}
    ttk::style element create Combobox.arrow image $I(down) -width 34 -sticky {}

    # Spinbox
    ttk::style layout TSpinbox {
      Spinbox.field -side top -sticky we -children {
        Spinbox.downarrow -side right -sticky ns
        Spinbox.uparrow -side right -sticky ns
        Spinbox.padding -sticky nswe -children {
          Spinbox.textarea -sticky nsew
        }
      }
    }

    ttk::style configure TSpinbox -foreground $colors(-fg) -padding {6 1 0 2}
    ttk::style map TSpinbox -foreground [list disabled "#757575" pressed "#cfcfcf"]

    ttk::style element create Spinbox.field image \
      [list $I(textbox-rest) \
        {focus hover !invalid} $I(textbox-focus) \
        invalid $I(textbox-error) \
        disabled $I(textbox-dis) \
        focus $I(textbox-focus) \
        {focus !invalid} $I(textbox-focus) \
        hover $I(button-focus) \
      ] -border 5 -sticky nsew

    ttk::style element create Spinbox.uparrow image $I(up) -width 34 -height 16 -sticky {}
    ttk::style element create Spinbox.downarrow image $I(down) -width 34 -height 16 -sticky {}

    # Progressbar
    ttk::style element create Horizontal.Progressbar.trough image $I(progressbar-trough-hor) -border 1 -sticky ew
    ttk::style element create Horizontal.Progressbar.pbar image $I(progressbar-bar-hor) -border 2 -sticky ew

    ttk::style element create Vertical.Progressbar.trough image $I(progressbar-trough-vert) -border 1 -sticky ns
    ttk::style element create Vertical.Progressbar.pbar image $I(progressbar-bar-vert) -border 2 -sticky ns

    # Scale
    ttk::style element create Horizontal.Scale.trough image $I(slider-trough-hor) \
      -border 5 -padding 0 -sticky {ew}

    ttk::style element create Vertical.Scale.trough image $I(slider-trough-vert) \
      -border 5 -padding 0 -sticky {ns}

    ttk::style element create Scale.slider image \
      [list $I(slider-thumb-rest) \
        disabled $I(slider-thumb-dis) \
        pressed $I(slider-thumb-pressed) \
        {active focus} $I(slider-thumb-focus-hover) \
        active $I(slider-thumb-hover) \
        focus $I(slider-thumb-focus) \
      ] -sticky {}

    # Scrollbar
    ttk::style layout Vertical.TScrollbar {
      Vertical.Scrollbar.trough -sticky ns -children {
        Vertical.Scrollbar.uparrow -side top
        Vertical.Scrollbar.downarrow -side bottom
        Vertical.Scrollbar.thumb -expand 1
      }
    }

    ttk::style layout Horizontal.TScrollbar {
      Horizontal.Scrollbar.trough -sticky ew -children {
        Horizontal.Scrollbar.leftarrow -side left
        Horizontal.Scrollbar.rightarrow -side right
        Horizontal.Scrollbar.thumb -expand 1
      }
    }

    ttk::style element create Horizontal.Scrollbar.trough image $I(scrollbar-trough-hor) -sticky ew -border 6
    ttk::style element create Horizontal.Scrollbar.thumb image $I(scrollbar-thumb-hor) -sticky ew -border 3

    ttk::style element create Horizontal.Scrollbar.rightarrow image $I(scrollbar-right) -sticky e -width 13
    ttk::style element create Horizontal.Scrollbar.leftarrow image $I(scrollbar-left) -sticky w -width 13

    ttk::style element create Vertical.Scrollbar.trough image $I(scrollbar-trough-vert) -sticky ns -border 6
    ttk::style element create Vertical.Scrollbar.thumb image $I(scrollbar-thumb-vert) -sticky ns -border 3

    ttk::style element create Vertical.Scrollbar.uparrow image $I(scrollbar-up) -sticky n -height 13
    ttk::style element create Vertical.Scrollbar.downarrow image $I(scrollbar-down) -sticky s -height 13

    # Separator
    ttk::style element create Separator.separator image $I(sep) -width 1 -height 1

    # Sizegrip
    ttk::style element create Sizegrip.sizegrip image $I(grip) -sticky nsew

    # Card
    ttk::style layout Card.TFrame {
      Card.field {
        Card.padding -expand 1 
      }
    }

    ttk::style element create Card.field image $I(card) -border 10 -padding 4 -sticky nsew

    # Labelframe
    ttk::style layout TLabelframe {
      Labelframe.border {
        Labelframe.padding -expand 1 -children {
          Labelframe.label -side left
        }
      }
    }

    ttk::style element create Labelframe.border image $I(card) -border 5 -padding 4 -sticky nsew
    ttk::style configure TLabelframe.Label -font SunValleyCaptionFont

    # Notebook
    ttk::style layout TNotebook {
      Notebook.border -children {
        TNotebook.Tab -expand 1
      }
    }

    ttk::style configure TNotebook -padding 1
    ttk::style configure TNotebook.Tab -focuscolor $colors(-accent)
    ttk::style element create Notebook.border image $I(notebook-border) -border 5 -padding 5

    ttk::style element create Notebook.tab image \
      [list $I(tab-rest) \
        selected $I(tab-selected-copia) \
        active $I(tab-hover) \
      ] -border 13 -padding {16 14 16 6} -height 32

    # Treeview
    ttk::style configure Heading -font SunValleyCaptionFont
    ttk::style configure Treeview \
        -background $colors(-bg) \
        -rowheight [expr {[font metrics SunValleyBodyFont -linespace] + 3}] \
        -font SunValleyBodyFont    

    ttk::style element create Treeview.field image $I(card) -border 5 -width 0 -height 0
    
    ttk::style element create Treeheading.cell image \
      [list $I(heading-rest) \
        pressed $I(box-accent) \
        active $I(button-focus)
      ] -border 5 -padding 14 -sticky nsew
    
    ttk::style element create Treeitem.indicator image \
      [list $I(right) \
        user2 $I(empty) \
        user1 $I(down) \
      ] -width 26 -sticky {}

    ttk::style map Treeview \
            -background [list selected $colors(-accent)] \
            -foreground [list selected $colors(-selectfg)]
  

    # Dialog
    ttk::style layout Dialog_buttons.TFrame {
      Dialog_buttons.field {
          Dialog_buttons -expand 1 
      }
    }        
    
    ttk::style element create Dialog_buttons.field image $I(card2) \
      -border 10 -padding 4 -sticky nsew  

    # Panedwindow
    ttk::style configure Sash \
      -lightcolor "#9e9e9e" \
      -darkcolor "#9e9e9e" \
      -bordercolor "#9e9e9e" \
      -sashthickness 4 \
      -gripcount 20

    # Sashes
    #ttk::style map TPanedwindow -background [list hover $colors(-bg)]  
  }
}
