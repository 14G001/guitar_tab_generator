from window.gui.element.menuBar import setMenuBarOptAction
from window.gui.window.type.secondMainWin import Ui_SecondMainWindow
from window.gui.style.size import setElementSize
from window.gui.window.window import GUIWindow
from window.gui.event.window import showWindow, closeWindow
from window.window.subWindow.singleInput.textLine.saveConfig import SaveConfigWindow
from window.window.subWindow.singleInput.comboBox.restoreConfig import RestoreConfigWindow
from window.window.subWindow.singleInput.comboBox.removeConfig import RemoveConfigWindow
from window.window.element.secondMainWinMenuButton import SndMainWinMenuButton
from window.window.element.input.color import ColorInput
from window.window.element.input.line.number.bpm import BPMInput
from window.window.element.input.comboBox import ComboBox
from window.window.element.input.checkBox.defaultCheckBox import DefaultCheckBox
from window.window.element.input.checkBox.metronomeCheckBox import MetronomeCheckBox
from window.window.element.input.file.audioFileInput import AudioFileInput
from window.window.element.input.file.imageFileInput import ImageFileInput
from window.window.element.input.file.tabsFileInput import TabsFileInput
from window.window.element.toolTip.warningToolTip import setWarningToolTip
from configs.configs import Configs


AUX_COMBO_BOX_ELEMENTS = ("opalo", "fruta", "verdura")


class MainWindow:
    def __init__(self, gui):
        self.extraWindow = None
        self.createSecondaryMainWindow()
        self.initMainWindow(gui)
        self.initSecondaryMainWindow()
        self.initInputElements()
    
    def createSecondaryMainWindow(self):
        self.sndWin = GUIWindow(Ui_SecondMainWindow())

    def setExtraWindow(self, window):
        if self.extraWindow != None:
            closeWindow(self.extraWindow)
        self.extraWindow = window
    def initMainWindow(self, gui):
        setMenuBarOptAction(gui.aMoreOptions,  lambda: showWindow(self.sndWin))

        setMenuBarOptAction(gui.aSaveConfig,   lambda: self.setExtraWindow(SaveConfigWindow()))
        setMenuBarOptAction(gui.aRestoreConfig,lambda: self.setExtraWindow(RestoreConfigWindow()))
        setMenuBarOptAction(gui.aDeleteConfig, lambda: self.setExtraWindow(RemoveConfigWindow()))
        setMenuBarOptAction(gui.aResetDefault, lambda: Configs().setDefault())

        self.bTabsFile =        TabsFileInput("TabsFile", [gui.bTabsFile])
        self.eBPM =             BPMInput("BPM",           (gui.eBPM,                  self.sndWin.window.eBPM))
        self.cNotesPerBeat =    ComboBox("NotesPerBeat",  (gui.cNotesPerBeat,         self.sndWin.window.cNotesPerBeat), AUX_COMBO_BOX_ELEMENTS)
        self.lFretColor =       ColorInput("FretColor",   (gui.lFretColor,            self.sndWin.window.lFretColor))
        self.lPlayedFretColor = ColorInput("PlayedFretColor", (gui.lPlayedFretColor,  self.sndWin.window.lPlayedFretColor))
        self.bGoPremium =       gui.bGoPremium
        self.bDonate =          gui.bDonate
        self.bGenerateTabs =    gui.bGenerateTabs

    def initSecondaryMainWindow(self):
        self.menuColors =     SndMainWinMenuButton(self.sndWin.gui, self.sndWin.window.menuColors,      self.sndWin.window.menuColorsBG    )
        self.menuAudio =      SndMainWinMenuButton(self.sndWin.gui, self.sndWin.window.menuAudio,       self.sndWin.window.menuAudioBG     )
        self.menuSongSpeed =  SndMainWinMenuButton(self.sndWin.gui, self.sndWin.window.menuSongSpeed,   self.sndWin.window.menuSongSpeedBG )
        self.menuFormats =    SndMainWinMenuButton(self.sndWin.gui, self.sndWin.window.menuFormats,     self.sndWin.window.menuFormatsBG   )
        self.menuBackground = SndMainWinMenuButton(self.sndWin.gui, self.sndWin.window.menuBackground,  self.sndWin.window.menuBackgroundBG)

        setElementSize(self.sndWin.gui, (500, 300))

        self.lTuneColor =       ColorInput("TuneColor",    [self.sndWin.window.lTuneColor])
        self.lActionsColor =    ColorInput("ActionsColor", [self.sndWin.window.lActionsColor])

        self.cbDefaultDrums =   DefaultCheckBox("HasDefaultDrums",  [self.sndWin.window.cbDefaultDrums],     [self.sndWin.window.cbCustomAudio])
        setWarningToolTip(self.sndWin.window.bCustomAudioWarning, "You should set an audio at the same tempo as BPM setted and you should make sure audio its at the same tempo. If audio you are submitting is at no tempo or is not at the same tempo as the setted BPM; music and tabs will be unsynchronized.")
        self.cbCustomAudio =    DefaultCheckBox("HasCustomAudio",   [self.sndWin.window.cbCustomAudio],      [self.sndWin.window.cbDefaultDrums])
        self.bCustomAudioFile = AudioFileInput("CustomAudioFile",   [self.sndWin.window.bCustomAudioFile],   [self.cbCustomAudio])    
        self.cbMainMetronome =  DefaultCheckBox("HasMainMetronome", [self.sndWin.window.cbMainMetronome])
        self.bBPM =             MetronomeCheckBox([self.sndWin.window.bBPM])
        
        self.cNoteFormat =      ComboBox("NoteFormat", [self.sndWin.window.cNoteFormat],   AUX_COMBO_BOX_ELEMENTS)
        self.cTabSize =         ComboBox("TabSize",    [self.sndWin.window.cTabSize],      AUX_COMBO_BOX_ELEMENTS)
        self.eFPS =             BPMInput("FPS",        [self.sndWin.window.eFPS])

        self.lBGColor =         ColorInput("BackgroundColor",         [self.sndWin.window.lBGColor])
        self.cbBGImage =        DefaultCheckBox("BackgroundImage",    [self.sndWin.window.cbBGImage])
        self.bBGImageFile =     ImageFileInput("BackgroundImageFile", [self.sndWin.window.bBGImageFile], [self.cbBGImage])

    def initInputElements(self):
        self.inputElements = (
            self.bTabsFile,
            self.eBPM,
            self.cNotesPerBeat,
            self.lFretColor,
            self.lPlayedFretColor,
            self.lTuneColor,
            self.lActionsColor,
            self.cbDefaultDrums,
            self.cbCustomAudio,
            self.bCustomAudioFile,
            self.cbMainMetronome,
            self.cNoteFormat,
            self.cTabSize,
            self.eFPS,
            self.lBGColor,
            self.cbBGImage,
            self.bBGImageFile
        )