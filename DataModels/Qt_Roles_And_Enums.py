import QT
Qt    = QT.Qt
QtGui = QT.QtGui
########################################################################
class AbstractItemView:
	########################################################################
	class Drag_Drop_Mode:
		DragDrop     = QT.QAbstractItemView.DragDrop
		DragOnly     = QT.QAbstractItemView.DragOnly
		DropOnly     = QT.QAbstractItemView.DropOnly
		InternalMove = QT.QAbstractItemView.InternalMove
		NoDragDrop   = QT.QAbstractItemView.NoDragDrop
	########################################################################
	class CursorAction:
		Down     = QT.QAbstractItemView.MoveDown
		Up       = QT.QAbstractItemView.MoveUp
		Left     = QT.QAbstractItemView.MoveLeft
		Right    = QT.QAbstractItemView.MoveRight
		Home     = QT.QAbstractItemView.MoveHome
		End      = QT.QAbstractItemView.MoveEnd
		Next     = QT.QAbstractItemView.MoveNext
		Previous = QT.QAbstractItemView.MovePrevious
		PageUp   = QT.QAbstractItemView.MovePageUp
		PageDown = QT.QAbstractItemView.MovePageDown
	########################################################################
	class DropIndicatorPosition:
		AboveItem  = QT.QAbstractItemView.AboveItem
		BelowItem  = QT.QAbstractItemView.BelowItem
		OnItem     = QT.QAbstractItemView.OnItem
		OnViewport = QT.QAbstractItemView.OnViewport
	########################################################################
	class EditTrigger:
		AllEditTriggers = QT.QAbstractItemView.AllEditTriggers
		AnyKeyPressed   = QT.QAbstractItemView.AnyKeyPressed
		CurrentChanged  = QT.QAbstractItemView.CurrentChanged
		DoubleClicked   = QT.QAbstractItemView.DoubleClicked
		EditKeyPressed  = QT.QAbstractItemView.EditKeyPressed
		NoEditTriggers  = QT.QAbstractItemView.NoEditTriggers
		SelectedClicked = QT.QAbstractItemView.SelectedClicked
	########################################################################
	class ScrollHint:
		EnsureVisible    = QT.QAbstractItemView.EnsureVisible
		PositionAtBottom = QT.QAbstractItemView.PositionAtBottom
		PositionAtCenter = QT.QAbstractItemView.PositionAtCenter
		PositionAtTop    = QT.QAbstractItemView.PositionAtTop
	########################################################################
	class ScrollMode:
		PerItem  = QT.QAbstractItemView.ScrollPerItem
		PerPixel = QT.QAbstractItemView.ScrollPerPixel
	########################################################################
	class SelectionBehavior:
		Columns = QT.QAbstractItemView.SelectColumns
		Items   = QT.QAbstractItemView.SelectItems
		Rows    = QT.QAbstractItemView.SelectRows
	########################################################################
	class SelectionMode:
		Contiguous = QT.QAbstractItemView.ContiguousSelection
		Extended   = QT.QAbstractItemView.ExtendedSelection
		Multi      = QT.QAbstractItemView.MultiSelection
		No         = QT.QAbstractItemView.NoSelection
		Single     = QT.QAbstractItemView.SingleSelection
	########################################################################
	class Shadow:
		Plain  = QT.QAbstractItemView.Plain
		Raised = QT.QAbstractItemView.Raised
		Sunken = QT.QAbstractItemView.Sunken
	########################################################################	
	class Shape:
		Box         = QT.QAbstractItemView.Box
		HLine       = QT.QAbstractItemView.HLine
		NoFrame     = QT.QAbstractItemView.NoFrame
		Panel       = QT.QAbstractItemView.Panel
		StyledPanel = QT.QAbstractItemView.StyledPanel
		VLine       = QT.QAbstractItemView.VLine
		WinPanel    = QT.QAbstractItemView.WinPanel
	########################################################################
	class State:
		Animating     = QT.QAbstractItemView.AnimatingState
		Collapsing    = QT.QAbstractItemView.CollapsingState
		DragSelecting = QT.QAbstractItemView.DragSelectingState
		Dragging      = QT.QAbstractItemView.DraggingState
		Editing       = QT.QAbstractItemView.EditingState
		Expanding     = QT.QAbstractItemView.ExpandingState
		No            = QT.QAbstractItemView.NoState
		
########################################################################
class Constants:
	# ########################################################################
	# class AnchorAttribute:
		# AnchorName = Qt.AnchorName
		# AnchorHref = Qt.AnchorHref
	########################################################################
	class AnchorPoint:
		AnchorBottom           = Qt.AnchorBottom
		AnchorRight            = Qt.AnchorRight
		AnchorLeft             = Qt.AnchorLeft
		AnchorHorizontalCenter = Qt.AnchorHorizontalCenter
		AnchorTop              = Qt.AnchorTop
		AnchorVerticalCenter   = Qt.AnchorVerticalCenter
	########################################################################
	class ApplicationAttribute:
		AA_DontShowIconsInMenus             = Qt.AA_DontShowIconsInMenus
		AA_DontUseNativeMenuBar             = Qt.AA_DontUseNativeMenuBar
		AA_NativeWindows                    = Qt.AA_NativeWindows
		AA_ImmediateWidgetCreation          = Qt.AA_ImmediateWidgetCreation
		AA_MSWindowsUseDirect3DByDefault    = Qt.AA_MSWindowsUseDirect3DByDefault
		# AA_S60DontConstructApplicationPanes = Qt.AA_DontConstructApplicationPanes
		AA_DontCreateNativeWidgetSiblings   = Qt.AA_DontCreateNativeWidgetSiblings
		AA_MacDontSwapCtrlAndMeta           = Qt.AA_MacDontSwapCtrlAndMeta
		AA_MacPluginApplication             = Qt.AA_MacPluginApplication
	########################################################################
	class ArrowType:
		RightArrow = Qt.RightArrow
		NoArrow    = Qt.NoArrow
		UpArrow    = Qt.UpArrow
		DownArrow  = Qt.DownArrow
		LeftArrow  = Qt.LeftArrow
	########################################################################
	class AspectRatioMode:
		IgnoreAspectRatio          = Qt.IgnoreAspectRatio
		KeepAspectRatio            = Qt.KeepAspectRatio
		KeepAspectRatioByExpanding = Qt.KeepAspectRatioByExpanding
	########################################################################
	class Axis:
		ZAxis = Qt.ZAxis
		XAxis = Qt.XAxis
		YAxis = Qt.YAxis
	########################################################################
	class BGMode:
		TransparentMode = Qt.TransparentMode
		OpaqueMode      = Qt.OpaqueMode
	########################################################################
	class CaseSensitivity:
		CaseSensitive   = Qt.CaseSensitive
		CaseInsensitive = Qt.CaseInsensitive
	########################################################################
	class ClipOperation:
		# UniteClip     = Qt.UniteClip
		ReplaceClip   = Qt.ReplaceClip
		IntersectClip = Qt.IntersectClip
		NoClip        = Qt.NoClip
	########################################################################
	class ConnectionType:
		UniqueConnection         = Qt.UniqueConnection
		AutoConnection           = Qt.AutoConnection
		BlockingQueuedConnection = Qt.BlockingQueuedConnection
		QueuedConnection         = Qt.QueuedConnection
		# AutoCompatConnection     = Qt.AutoCompatConnection
		DirectConnection         = Qt.DirectConnection
	########################################################################
	class ContextMenuPolicy:
		DefaultContextMenu = Qt.DefaultContextMenu
		PreventContextMenu = Qt.PreventContextMenu
		ActionsContextMenu = Qt.ActionsContextMenu
		NoContextMenu      = Qt.NoContextMenu
		CustomContextMenu  = Qt.CustomContextMenu
	########################################################################
	class CoordinateSystem:
		LogicalCoordinates = Qt.LogicalCoordinates
		DeviceCoordinates  = Qt.DeviceCoordinates
	########################################################################
	class Corner:
		TopRightCorner    = Qt.TopRightCorner
		BottomRightCorner = Qt.BottomRightCorner
		TopLeftCorner     = Qt.TopLeftCorner
		BottomLeftCorner  = Qt.BottomLeftCorner
	########################################################################
	class CursorShape:
		DragCopyCursor     = Qt.DragCopyCursor
		CrossCursor        = Qt.CrossCursor
		SizeFDiagCursor    = Qt.SizeFDiagCursor
		SizeAllCursor      = Qt.SizeAllCursor
		SizeHorCursor      = Qt.SizeHorCursor
		UpArrowCursor      = Qt.UpArrowCursor
		CustomCursor       = Qt.CustomCursor
		LastCursor         = Qt.LastCursor
		BusyCursor         = Qt.BusyCursor
		OpenHandCursor     = Qt.OpenHandCursor
		SizeVerCursor      = Qt.SizeVerCursor
		WhatsThisCursor    = Qt.WhatsThisCursor
		BitmapCursor       = Qt.BitmapCursor
		DragMoveCursor     = Qt.DragMoveCursor
		DragLinkCursor     = Qt.DragLinkCursor
		IBeamCursor        = Qt.IBeamCursor
		ArrowCursor        = Qt.ArrowCursor
		SplitVCursor       = Qt.SplitVCursor
		WaitCursor         = Qt.WaitCursor
		BlankCursor        = Qt.BlankCursor
		PointingHandCursor = Qt.PointingHandCursor
		ForbiddenCursor    = Qt.ForbiddenCursor
		SizeBDiagCursor    = Qt.SizeBDiagCursor
		SplitHCursor       = Qt.SplitHCursor
		ClosedHandCursor   = Qt.ClosedHandCursor
	########################################################################
	class DateFormat:
		DefaultLocaleLongDate  = Qt.DefaultLocaleLongDate
		TextDate               = Qt.TextDate
		LocaleDate             = Qt.LocaleDate
		ISODate                = Qt.ISODate
		DefaultLocaleShortDate = Qt.DefaultLocaleShortDate
		SystemLocaleShortDate  = Qt.SystemLocaleShortDate
		LocalDate              = Qt.LocalDate
		SystemLocaleDate       = Qt.SystemLocaleDate
		SystemLocaleLongDate   = Qt.SystemLocaleLongDate
	########################################################################
	class DockWidgetArea:
		AllDockWidgetAreas   = Qt.AllDockWidgetAreas
		LeftDockWidgetArea   = Qt.LeftDockWidgetArea
		DockWidgetArea_Mask  = Qt.DockWidgetArea_Mask
		NoDockWidgetArea     = Qt.NoDockWidgetArea
		TopDockWidgetArea    = Qt.TopDockWidgetArea
		RightDockWidgetArea  = Qt.RightDockWidgetArea
		BottomDockWidgetArea = Qt.BottomDockWidgetArea
	########################################################################
	class DropAction:
		LinkAction       = Qt.LinkAction
		CopyAction       = Qt.CopyAction
		IgnoreAction     = Qt.IgnoreAction
		TargetMoveAction = Qt.TargetMoveAction
		MoveAction       = Qt.MoveAction
		ActionMask       = Qt.ActionMask
	########################################################################
	class EventPriority:
		NormalEventPriority = Qt.NormalEventPriority
		HighEventPriority   = Qt.HighEventPriority
		LowEventPriority    = Qt.LowEventPriority
	########################################################################
	class FillRule:
		WindingFill = Qt.WindingFill
		OddEvenFill = Qt.OddEvenFill
	########################################################################
	class FocusPolicy:
		StrongFocus = Qt.StrongFocus
		WheelFocus  = Qt.WheelFocus
		ClickFocus  = Qt.ClickFocus
		TabFocus    = Qt.TabFocus
		NoFocus     = Qt.NoFocus
	########################################################################
	class FocusReason:
		NoFocusReason           = Qt.NoFocusReason
		BacktabFocusReason      = Qt.BacktabFocusReason
		ShortcutFocusReason     = Qt.ShortcutFocusReason
		PopupFocusReason        = Qt.PopupFocusReason
		MouseFocusReason        = Qt.MouseFocusReason
		ActiveWindowFocusReason = Qt.ActiveWindowFocusReason
		MenuBarFocusReason      = Qt.MenuBarFocusReason
		TabFocusReason          = Qt.TabFocusReason
		OtherFocusReason        = Qt.OtherFocusReason
	########################################################################
	class GestureFlag:
		DontStartGestureOnChildren       = Qt.DontStartGestureOnChildren
		ReceivePartialGestures           = Qt.ReceivePartialGestures
		IgnoredGesturesPropagateToParent = Qt.IgnoredGesturesPropagateToParent
	########################################################################
	class GestureState:
		GestureUpdated  = Qt.GestureUpdated
		GestureFinished = Qt.GestureFinished
		GestureCanceled = Qt.GestureCanceled
		GestureStarted  = Qt.GestureStarted
	########################################################################
	class GestureType:
		SwipeGesture      = Qt.SwipeGesture
		CustomGesture     = Qt.CustomGesture
		PinchGesture      = Qt.PinchGesture
		TapAndHoldGesture = Qt.TapAndHoldGesture
		TapGesture        = Qt.TapGesture
		PanGesture        = Qt.PanGesture
	########################################################################
	class GlobalColor:
		lightGray   = Qt.lightGray
		gray        = Qt.gray
		darkGreen   = Qt.darkGreen
		darkMagenta = Qt.darkMagenta
		darkCyan    = Qt.darkCyan
		darkBlue    = Qt.darkBlue
		darkGray    = Qt.darkGray
		blue        = Qt.blue
		yellow      = Qt.yellow
		darkYellow  = Qt.darkYellow
		color1      = Qt.color1
		color0      = Qt.color0
		transparent = Qt.transparent
		black       = Qt.black
		darkRed     = Qt.darkRed
		cyan        = Qt.cyan
		green       = Qt.green
		white       = Qt.white
		magenta     = Qt.magenta
		red         = Qt.red
	########################################################################
	class HitTestAccuracy:
		FuzzyHit = Qt.FuzzyHit
		ExactHit = Qt.ExactHit
	########################################################################
	class ImageConversionFlag:
		AvoidDither          = Qt.AvoidDither
		AutoColor            = Qt.AutoColor
		OrderedDither        = Qt.OrderedDither 
		PreferDither         = Qt.PreferDither
		OrderedAlphaDither   = Qt.OrderedAlphaDither
		ThresholdAlphaDither = Qt.ThresholdAlphaDither
		DiffuseAlphaDither   = Qt.DiffuseAlphaDither
		DiffuseDither        = Qt.DiffuseDither
		AutoDither           = Qt.AutoDither
		ColorOnly            = Qt.ColorOnly
		MonoOnly             = Qt.MonoOnly
		ThresholdDither      = Qt.ThresholdDither
	########################################################################
	class InputMethodHint:
		ImhPreferNumbers          = Qt.ImhPreferNumbers
		ImhDialableCharactersOnly = Qt.ImhDialableCharactersOnly
		ImhNoAutoUppercase        = Qt.ImhNoAutoUppercase
		ImhLowercaseOnly          = Qt.ImhLowercaseOnly
		ImhEmailCharactersOnly    = Qt.ImhEmailCharactersOnly
		ImhNoPredictiveText       = Qt.ImhNoPredictiveText
		ImhUrlCharactersOnly      = Qt.ImhUrlCharactersOnly
		ImhUppercaseOnly          = Qt.ImhUppercaseOnly
		ImhPreferUppercase        = Qt.ImhPreferUppercase
		ImhDigitsOnly             = Qt.ImhDigitsOnly
		ImhFormattedNumbersOnly   = Qt.ImhFormattedNumbersOnly
		ImhPreferLowercase        = Qt.ImhPreferLowercase
		ImhHiddenText             = Qt.ImhHiddenText
		ImhNone                   = Qt.ImhNone
		ImhExclusiveInputMask     = Qt.ImhExclusiveInputMask
	########################################################################
	class InputMethodQuery:
		ImCursorPosition    = Qt.ImCursorPosition
		ImFont              = Qt.ImFont
		ImAnchorPosition    = Qt.ImAnchorPosition
		ImMicroFocus        = Qt.ImMicroFocus
		ImMaximumTextLength = Qt.ImMaximumTextLength
		ImSurroundingText   = Qt.ImSurroundingText
		ImCurrentSelection  = Qt.ImCurrentSelection
	########################################################################
	class ItemSelectionMode:
		ContainsItemBoundingRect   = Qt.ContainsItemBoundingRect
		IntersectsItemBoundingRect = Qt.IntersectsItemBoundingRect
		ContainsItemShape          = Qt.ContainsItemShape
		IntersectsItemShape        = Qt.IntersectsItemShape
	########################################################################
	class Key:
		Excel                  = Qt.Key_Excel
		hyphen                 = Qt.Key_hyphen
		Space                  = Qt.Key_Space
		Pause                  = Qt.Key_Pause
		F27                    = Qt.Key_F27
		F26                    = Qt.Key_F26
		F25                    = Qt.Key_F25
		F24                    = Qt.Key_F24
		F23                    = Qt.Key_F23
		F22                    = Qt.Key_F22
		F21                    = Qt.Key_F21
		F20                    = Qt.Key_F20
		DOS                    = Qt.Key_DOS
		F29                    = Qt.Key_F29
		F28                    = Qt.Key_F28
		OpenUrl                = Qt.Key_OpenUrl
		Launch8                = Qt.Key_Launch8
		Launch9                = Qt.Key_Launch9
		Dead_Belowdot          = Qt.Key_Dead_Belowdot
		onequarter             = Qt.Key_onequarter
		HomePage               = Qt.Key_HomePage
		Launch1                = Qt.Key_Launch1
		Launch2                = Qt.Key_Launch2
		Launch3                = Qt.Key_Launch3
		Launch4                = Qt.Key_Launch4
		Launch5                = Qt.Key_Launch5
		Launch6                = Qt.Key_Launch6
		Launch7                = Qt.Key_Launch7
		LaunchH                = Qt.Key_LaunchH
		Ediaeresis             = Qt.Key_Ediaeresis
		Shift                  = Qt.Key_Shift
		LaunchA                = Qt.Key_LaunchA
		LaunchB                = Qt.Key_LaunchB
		LaunchC                = Qt.Key_LaunchC
		LaunchD                = Qt.Key_LaunchD
		LaunchE                = Qt.Key_LaunchE
		LaunchF                = Qt.Key_LaunchF
		LaunchG                = Qt.Key_LaunchG
		Left                   = Qt.Key_Left
		Dead_Caron             = Qt.Key_Dead_Caron
		Hangul_Special         = Qt.Key_Hangul_Special
		Hangul_Jamo            = Qt.Key_Hangul_Jamo
		Period                 = Qt.Key_Period
		Dead_Voiced_Sound      = Qt.Key_Dead_Voiced_Sound
		Ooblique               = Qt.Key_Ooblique
		OfficeHome             = Qt.Key_OfficeHome
		Colon                  = Qt.Key_Colon
		Forward                = Qt.Key_Forward
		UWB                    = Qt.Key_UWB
		Katakana               = Qt.Key_Katakana
		Eisu_toggle            = Qt.Key_Eisu_toggle
		Zoom                   = Qt.Key_Zoom
		Zenkaku                = Qt.Key_Zenkaku
		Save                   = Qt.Key_Save
		Greater                = Qt.Key_Greater
		WebCam                 = Qt.Key_WebCam
		VolumeMute             = Qt.Key_VolumeMute
		ParenRight             = Qt.Key_ParenRight
		MenuKB                 = Qt.Key_MenuKB
		Video                  = Qt.Key_Video
		Oacute                 = Qt.Key_Oacute
		NumLock                = Qt.Key_NumLock
		Multi_key              = Qt.Key_Multi_key
		Ugrave                 = Qt.Key_Ugrave
		Ccedilla               = Qt.Key_Ccedilla
		Dead_Horn              = Qt.Key_Dead_Horn
		Hangul_Hanja           = Qt.Key_Hangul_Hanja
		Call                   = Qt.Key_Call
		AudioForward           = Qt.Key_AudioForward
		macron                 = Qt.Key_macron
		section                = Qt.Key_section
		Away                   = Qt.Key_Away
		MenuPB                 = Qt.Key_MenuPB
		Hangul_Jeonja          = Qt.Key_Hangul_Jeonja
		Equal                  = Qt.Key_Equal
		Standby                = Qt.Key_Standby
		TrebleDown             = Qt.Key_TrebleDown
		Launch0                = Qt.Key_Launch0
		Hankaku                = Qt.Key_Hankaku
		Enter                  = Qt.Key_Enter
		Dead_Semivoiced_Sound  = Qt.Key_Dead_Semivoiced_Sound
		Dead_Tilde             = Qt.Key_Dead_Tilde
		ScreenSaver            = Qt.Key_ScreenSaver
		Less                   = Qt.Key_Less
		Game                   = Qt.Key_Game
		Alt                    = Qt.Key_Alt
		yen                    = Qt.Key_yen
		NumberSign             = Qt.Key_NumberSign
		AudioRewind            = Qt.Key_AudioRewind
		Hangul_Banja           = Qt.Key_Hangul_Banja
		Printer                = Qt.Key_Printer
		twosuperior            = Qt.Key_twosuperior
		Favorites              = Qt.Key_Favorites
		Exclam                 = Qt.Key_Exclam
		Xfer                   = Qt.Key_Xfer
		AltGr                  = Qt.Key_AltGr
		Kana_Lock              = Qt.Key_Kana_Lock
		Insert                 = Qt.Key_Insert
		guillemotright         = Qt.Key_guillemotright
		Subtitle               = Qt.Key_Subtitle
		KeyboardBrightnessUp   = Qt.Key_KeyboardBrightnessUp
		Market                 = Qt.Key_Market
		MediaPause             = Qt.Key_MediaPause
		Suspend                = Qt.Key_Suspend
		VolumeDown             = Qt.Key_VolumeDown
		Send                   = Qt.Key_Send
		ScrollLock             = Qt.Key_ScrollLock
		Travel                 = Qt.Key_Travel
		BassDown               = Qt.Key_BassDown
		ApplicationLeft        = Qt.Key_ApplicationLeft
		BassBoost              = Qt.Key_BassBoost
		Hiragana               = Qt.Key_Hiragana
		TaskPane               = Qt.Key_TaskPane
		MediaTogglePlayPause   = Qt.Key_MediaTogglePlayPause
		LastNumberRedial       = Qt.Key_LastNumberRedial
		Muhenkan               = Qt.Key_Muhenkan
		Option                 = Qt.Key_Option
		masculine              = Qt.Key_masculine
		H                      = Qt.Key_H
		Phone                  = Qt.Key_Phone
		AE                     = Qt.Key_AE
		Refresh                = Qt.Key_Refresh
		MailForward            = Qt.Key_MailForward
		Super_R                = Qt.Key_Super_R
		F34                    = Qt.Key_F34
		F35                    = Qt.Key_F35
		F30                    = Qt.Key_F30
		F31                    = Qt.Key_F31
		F32                    = Qt.Key_F32
		F33                    = Qt.Key_F33
		Super_L                = Qt.Key_Super_L
		Dollar                 = Qt.Key_Dollar
		ApplicationRight       = Qt.Key_ApplicationRight
		Backslash              = Qt.Key_Backslash
		Community              = Qt.Key_Community
		At                     = Qt.Key_At
		Comma                  = Qt.Key_Comma
		notsign                = Qt.Key_notsign
		LightBulb              = Qt.Key_LightBulb
		questiondown           = Qt.Key_questiondown
		QuoteLeft              = Qt.Key_QuoteLeft
		Hangul_PreHanja        = Qt.Key_Hangul_PreHanja
		Hangul_Romaja          = Qt.Key_Hangul_Romaja
		Calculator             = Qt.Key_Calculator
		ClearGrab              = Qt.Key_ClearGrab
		Eisu_Shift             = Qt.Key_Eisu_Shift
		cent                   = Qt.Key_cent
		Messenger              = Qt.Key_Messenger
		Paste                  = Qt.Key_Paste
		BraceRight             = Qt.Key_BraceRight
		Stop                   = Qt.Key_Stop
		Sleep                  = Qt.Key_Sleep
		KeyboardLightOnOff     = Qt.Key_KeyboardLightOnOff
		VolumeUp               = Qt.Key_VolumeUp
		Ograve                 = Qt.Key_Ograve
		Hangul_Start           = Qt.Key_Hangul_Start
		Codeinput              = Qt.Key_Codeinput
		Yes                    = Qt.Key_Yes
		LaunchMedia            = Qt.Key_LaunchMedia
		exclamdown             = Qt.Key_exclamdown
		plusminus              = Qt.Key_plusminus
		Question               = Qt.Key_Question
		Context4               = Qt.Key_Context4
		Context3               = Qt.Key_Context3
		Context2               = Qt.Key_Context2
		Context1               = Qt.Key_Context1
		AsciiTilde             = Qt.Key_AsciiTilde
		BrightnessAdjust       = Qt.Key_BrightnessAdjust
		SingleCandidate        = Qt.Key_SingleCandidate
		Dead_Abovering         = Qt.Key_Dead_Abovering
		Finance                = Qt.Key_Finance
		Underscore             = Qt.Key_Underscore
		KeyboardBrightnessDown = Qt.Key_KeyboardBrightnessDown
		Dead_Breve             = Qt.Key_Dead_Breve
		Kanji                  = Qt.Key_Kanji
		sterling               = Qt.Key_sterling
		Eject                  = Qt.Key_Eject
		Copy                   = Qt.Key_Copy
		Display                = Qt.Key_Display
		WWW                    = Qt.Key_WWW
		HotLinks               = Qt.Key_HotLinks
		Agrave                 = Qt.Key_Agrave
		Cut                    = Qt.Key_Cut
		Idiaeresis             = Qt.Key_Idiaeresis
		acute                  = Qt.Key_acute
		CameraFocus            = Qt.Key_CameraFocus
		Dead_Macron            = Qt.Key_Dead_Macron
		RotationPB             = Qt.Key_RotationPB
		Hibernate              = Qt.Key_Hibernate
		Return                 = Qt.Key_Return
		Select                 = Qt.Key_Select
		Dead_Diaeresis         = Qt.Key_Dead_Diaeresis
		PowerDown              = Qt.Key_PowerDown
		BracketLeft            = Qt.Key_BracketLeft
		Minus                  = Qt.Key_Minus
		Apostrophe             = Qt.Key_Apostrophe
		Adiaeresis             = Qt.Key_Adiaeresis
		Shop                   = Qt.Key_Shop
		WakeUp                 = Qt.Key_WakeUp
		LaunchMail             = Qt.Key_LaunchMail
		End                    = Qt.Key_End
		Otilde                 = Qt.Key_Otilde
		TrebleUp               = Qt.Key_TrebleUp
		Pictures               = Qt.Key_Pictures
		BassUp                 = Qt.Key_BassUp
		Ntilde                 = Qt.Key_Ntilde
		Uacute                 = Qt.Key_Uacute
		Zenkaku_Hankaku        = Qt.Key_Zenkaku_Hankaku
		Play                   = Qt.Key_Play
		MySites                = Qt.Key_MySites
		Icircumflex            = Qt.Key_Icircumflex
		VoiceDial              = Qt.Key_VoiceDial
		Acircumflex            = Qt.Key_Acircumflex
		Dead_Grave             = Qt.Key_Dead_Grave
		Bar                    = Qt.Key_Bar
		Backtab                = Qt.Key_Backtab
		History                = Qt.Key_History
		multiply               = Qt.Key_multiply
		Dead_Acute             = Qt.Key_Dead_Acute
		AudioRepeat            = Qt.Key_AudioRepeat
		CapsLock               = Qt.Key_CapsLock
		Aring                  = Qt.Key_Aring
		PageDown               = Qt.Key_PageDown
		Calendar               = Qt.Key_Calendar
		ContrastAdjust         = Qt.Key_ContrastAdjust
		AudioCycleTrack        = Qt.Key_AudioCycleTrack
		Meeting                = Qt.Key_Meeting
		Terminal               = Qt.Key_Terminal
		threequarters          = Qt.Key_threequarters
		copyright              = Qt.Key_copyright
		unknown                = Qt.Key_unknown
		Asterisk               = Qt.Key_Asterisk
		iTouch                 = Qt.Key_iTouch
		Eacute                 = Qt.Key_Eacute
		periodcentered         = Qt.Key_periodcentered
		Camera                 = Qt.Key_Camera
		Flip                   = Qt.Key_Flip
		MediaNext              = Qt.Key_MediaNext
		Search                 = Qt.Key_Search
		Kana_Shift             = Qt.Key_Kana_Shift
		Igrave                 = Qt.Key_Igrave
		Battery                = Qt.Key_Battery
		Henkan                 = Qt.Key_Henkan
		Tools                  = Qt.Key_Tools
		Cancel                 = Qt.Key_Cancel
		Hangul_PostHanja       = Qt.Key_Hangul_PostHanja
		Any                    = Qt.Key_Any
		Hangul                 = Qt.Key_Hangul
		Ucircumflex            = Qt.Key_Ucircumflex
		Hangup                 = Qt.Key_Hangup
		ZoomOut                = Qt.Key_ZoomOut
		AddFavorite            = Qt.Key_AddFavorite
		Num_5                  = Qt.Key_5
		Num_4                  = Qt.Key_4
		Num_7                  = Qt.Key_7
		Num_6                  = Qt.Key_6
		Num_1                  = Qt.Key_1
		Num_0                  = Qt.Key_0
		Num_3                  = Qt.Key_3
		Num_2                  = Qt.Key_2
		Dead_Iota              = Qt.Key_Dead_Iota
		Num_9                  = Qt.Key_9
		Num_8                  = Qt.Key_8
		E                      = Qt.Key_E
		D                      = Qt.Key_D
		G                      = Qt.Key_G
		F                      = Qt.Key_F
		A                      = Qt.Key_A
		division               = Qt.Key_division
		C                      = Qt.Key_C
		B                      = Qt.Key_B
		M                      = Qt.Key_M
		L                      = Qt.Key_L
		O                      = Qt.Key_O
		N                      = Qt.Key_N
		I                      = Qt.Key_I
		Semicolon              = Qt.Key_Semicolon
		K                      = Qt.Key_K
		J                      = Qt.Key_J
		U                      = Qt.Key_U
		T                      = Qt.Key_T
		W                      = Qt.Key_W
		V                      = Qt.Key_V
		MediaRecord            = Qt.Key_MediaRecord
		P                      = Qt.Key_P
		S                      = Qt.Key_S
		R                      = Qt.Key_R
		Y                      = Qt.Key_Y
		X                      = Qt.Key_X
		Z                      = Qt.Key_Z
		F4                     = Qt.Key_F4
		F5                     = Qt.Key_F5
		F6                     = Qt.Key_F6
		F7                     = Qt.Key_F7
		F1                     = Qt.Key_F1
		F2                     = Qt.Key_F2
		F3                     = Qt.Key_F3
		F8                     = Qt.Key_F8
		F9                     = Qt.Key_F9
		Odiaeresis             = Qt.Key_Odiaeresis
		Escape                 = Qt.Key_Escape
		ydiaeresis             = Qt.Key_ydiaeresis
		Meta                   = Qt.Key_Meta
		Support                = Qt.Key_Support
		Documents              = Qt.Key_Documents
		Egrave                 = Qt.Key_Egrave
		nobreakspace           = Qt.Key_nobreakspace
		PowerOff               = Qt.Key_PowerOff
		Explorer               = Qt.Key_Explorer
		RotateWindows          = Qt.Key_RotateWindows
		MonBrightnessDown      = Qt.Key_MonBrightnessDown
		degree                 = Qt.Key_degree
		View                   = Qt.Key_View
		BraceLeft              = Qt.Key_BraceLeft
		Reload                 = Qt.Key_Reload
		threesuperior          = Qt.Key_threesuperior
		mu                     = Qt.Key_mu
		SysReq                 = Qt.Key_SysReq
		Menu                   = Qt.Key_Menu
		WLAN                   = Qt.Key_WLAN
		Dead_Hook              = Qt.Key_Dead_Hook
		Slash                  = Qt.Key_Slash
		ParenLeft              = Qt.Key_ParenLeft
		Iacute                 = Qt.Key_Iacute
		News                   = Qt.Key_News
		LogOff                 = Qt.Key_LogOff
		onehalf                = Qt.Key_onehalf
		Clear                  = Qt.Key_Clear
		Word                   = Qt.Key_Word
		Udiaeresis             = Qt.Key_Udiaeresis
		Romaji                 = Qt.Key_Romaji
		Time                   = Qt.Key_Time
		onesuperior            = Qt.Key_onesuperior
		MediaStop              = Qt.Key_MediaStop
		Bluetooth              = Qt.Key_Bluetooth
		Ocircumflex            = Qt.Key_Ocircumflex
		Right                  = Qt.Key_Right
		paragraph              = Qt.Key_paragraph
		Down                   = Qt.Key_Down
		Dead_Cedilla           = Qt.Key_Dead_Cedilla
		QuoteDbl               = Qt.Key_QuoteDbl
		Backspace              = Qt.Key_Backspace
		ZoomIn                 = Qt.Key_ZoomIn
		Reply                  = Qt.Key_Reply
		Dead_Ogonek            = Qt.Key_Dead_Ogonek
		Music                  = Qt.Key_Music
		Yacute                 = Qt.Key_Yacute
		Atilde                 = Qt.Key_Atilde
		ETH                    = Qt.Key_ETH
		Ecircumflex            = Qt.Key_Ecircumflex
		PageUp                 = Qt.Key_PageUp
		Hiragana_Katakana      = Qt.Key_Hiragana_Katakana
		CD                     = Qt.Key_CD
		cedilla                = Qt.Key_cedilla
		Execute                = Qt.Key_Execute
		F18                    = Qt.Key_F18
		F19                    = Qt.Key_F19
		F16                    = Qt.Key_F16
		F17                    = Qt.Key_F17
		F14                    = Qt.Key_F14
		F15                    = Qt.Key_F15
		F12                    = Qt.Key_F12
		F13                    = Qt.Key_F13
		F10                    = Qt.Key_F10
		F11                    = Qt.Key_F11
		Back                   = Qt.Key_Back
		Memo                   = Qt.Key_Memo
		Control                = Qt.Key_Control
		No                     = Qt.Key_No
		ordfeminine            = Qt.Key_ordfeminine
		Ampersand              = Qt.Key_Ampersand
		currency               = Qt.Key_currency
		Book                   = Qt.Key_Book
		BracketRight           = Qt.Key_BracketRight
		MonBrightnessUp        = Qt.Key_MonBrightnessUp
		Dead_Doubleacute       = Qt.Key_Dead_Doubleacute
		MultipleCandidate      = Qt.Key_MultipleCandidate
		TopMenu                = Qt.Key_TopMenu
		Touroku                = Qt.Key_Touroku
		Massyo                 = Qt.Key_Massyo
		Up                     = Qt.Key_Up
		MediaLast              = Qt.Key_MediaLast
		Hangul_End             = Qt.Key_Hangul_End
		Plus                   = Qt.Key_Plus
		AsciiCircum            = Qt.Key_AsciiCircum
		MediaPlay              = Qt.Key_MediaPlay
		Help                   = Qt.Key_Help
		Tab                    = Qt.Key_Tab
		Percent                = Qt.Key_Percent
		brokenbar              = Qt.Key_brokenbar
		Direction_R            = Qt.Key_Direction_R
		Print                  = Qt.Key_Print
		Direction_L            = Qt.Key_Direction_L
		RotationKB             = Qt.Key_RotationKB
		Aacute                 = Qt.Key_Aacute
		Spell                  = Qt.Key_Spell
		ToDoList               = Qt.Key_ToDoList
		SplitScreen            = Qt.Key_SplitScreen
		diaeresis              = Qt.Key_diaeresis
		PreviousCandidate      = Qt.Key_PreviousCandidate
		Home                   = Qt.Key_Home
		Hyper_L                = Qt.Key_Hyper_L
		Dead_Abovedot          = Qt.Key_Dead_Abovedot
		THORN                  = Qt.Key_THORN
		BackForward            = Qt.Key_BackForward
		Delete                 = Qt.Key_Delete
		registered             = Qt.Key_registered
		Hyper_R                = Qt.Key_Hyper_R
		Dead_Circumflex        = Qt.Key_Dead_Circumflex
		MediaPrevious          = Qt.Key_MediaPrevious
		ToggleCallHangup       = Qt.Key_ToggleCallHangup
		ssharp                 = Qt.Key_ssharp
		AudioRandomPlay        = Qt.Key_AudioRandomPlay
		Mode_switch            = Qt.Key_Mode_switch
		Close                  = Qt.Key_Close
		guillemotleft          = Qt.Key_guillemotleft
		Q                      = Qt.Key_Q
		Go                     = Qt.Key_Go
	########################################################################
	class LayoutDirection:
		RightToLeft         = Qt.RightToLeft
		LayoutDirectionAuto = Qt.LayoutDirectionAuto
		LeftToRight         = Qt.LeftToRight
	########################################################################
	class MouseButton:
		RightButton     = Qt.RightButton
		MiddleButton    = Qt.MiddleButton
		NoButton        = Qt.NoButton
		LeftButton      = Qt.LeftButton
		MouseButtonMask = Qt.MouseButtonMask
		XButton1        = Qt.XButton1
		XButton2        = Qt.XButton2
		MidButton       = Qt.MidButton
	########################################################################
	class Orientation:
		Horizontal = Qt.Horizontal
		Vertical   = Qt.Vertical
	########################################################################
	class PenCapStyle:
		FlatCap      = Qt.FlatCap
		RoundCap     = Qt.RoundCap
		SquareCap    = Qt.SquareCap
		MPenCapStyle = Qt.MPenCapStyle
	########################################################################
	class PenJoinStyle:
		RoundJoin     = Qt.RoundJoin
		MiterJoin     = Qt.MiterJoin
		MPenJoinStyle = Qt.MPenJoinStyle
		BevelJoin     = Qt.BevelJoin
		SvgMiterJoin  = Qt.SvgMiterJoin
	########################################################################
	class ScrollBarPolicy:
		AsNeeded  = Qt.ScrollBarAsNeeded
		AlwaysOff = Qt.ScrollBarAlwaysOff
		AlwaysOn  = Qt.ScrollBarAlwaysOn
	########################################################################
	class SizeHint:
		MinimumDescent = Qt.MinimumDescent
		PreferredSize  = Qt.PreferredSize
		MinimumSize    = Qt.MinimumSize
		MaximumSize    = Qt.MaximumSize
	########################################################################
	class SizeMode:
		AbsoluteSize = Qt.AbsoluteSize
		RelativeSize = Qt.RelativeSize
	########################################################################
	class SortOrder:
		Ascending  = Qt.AscendingOrder
		Descending = Qt.DescendingOrder
	########################################################################
	class TextFormat:
		PlainText = Qt.PlainText
		AutoText  = Qt.AutoText
		# LogText   = Qt.LogText
		RichText  = Qt.RichText
	########################################################################		
	class TextInteractionFlag:
		TextEditable              = Qt.TextEditable
		TextSelectableByKeyboard  = Qt.TextSelectableByKeyboard
		NoTextInteraction         = Qt.NoTextInteraction
		TextSelectableByMouse     = Qt.TextSelectableByMouse
		TextBrowserInteraction    = Qt.TextBrowserInteraction
		LinksAccessibleByKeyboard = Qt.LinksAccessibleByKeyboard
		LinksAccessibleByMouse    = Qt.LinksAccessibleByMouse
		TextEditorInteraction     = Qt.TextEditorInteraction
	########################################################################
	class TileRule:
		StretchTile = Qt.StretchTile
		RepeatTile  = Qt.RepeatTile
		RoundTile   = Qt.RoundTile
	########################################################################
	class TimeSpec:
		OffsetFromUTC = Qt.OffsetFromUTC
		UTC           = Qt.UTC
		LocalTime     = Qt.LocalTime
	########################################################################
	class ToolBarArea:
		RightToolBarArea  = Qt.RightToolBarArea
		TopToolBarArea    = Qt.TopToolBarArea
		ToolBarArea_Mask  = Qt.ToolBarArea_Mask
		NoToolBarArea     = Qt.NoToolBarArea
		LeftToolBarArea   = Qt.LeftToolBarArea
		AllToolBarAreas   = Qt.AllToolBarAreas
		BottomToolBarArea = Qt.BottomToolBarArea
	########################################################################
	class ToolButtonStyle:
		ToolButtonIconOnly       = Qt.ToolButtonIconOnly
		ToolButtonTextBesideIcon = Qt.ToolButtonTextBesideIcon
		ToolButtonTextOnly       = Qt.ToolButtonTextOnly
		ToolButtonFollowStyle    = Qt.ToolButtonFollowStyle
		ToolButtonTextUnderIcon  = Qt.ToolButtonTextUnderIcon
	########################################################################
	class TouchPointState:
		TouchPointReleased   = Qt.TouchPointReleased
		TouchPointPressed    = Qt.TouchPointPressed
		TouchPointMoved      = Qt.TouchPointMoved
		TouchPointStationary = Qt.TouchPointStationary
	########################################################################
	class UIEffect:
		AnimateCombo   = Qt.UI_AnimateCombo
		FadeMenu       = Qt.UI_FadeMenu
		AnimateTooltip = Qt.UI_AnimateTooltip
		AnimateMenu    = Qt.UI_AnimateMenu
		FadeTooltip    = Qt.UI_FadeTooltip
		General        = Qt.UI_General
		AnimateToolBox = Qt.UI_AnimateToolBox
	########################################################################
	class WhiteSpaceMode:
		WhiteSpaceNoWrap        = Qt.WhiteSpaceNoWrap
		WhiteSpaceModeUndefined = Qt.WhiteSpaceModeUndefined
		WhiteSpaceNormal        = Qt.WhiteSpaceNormal
		WhiteSpacePre           = Qt.WhiteSpacePre
	########################################################################
	class WidgetAttribute:
		CustomWhatsThis                 = Qt.WA_CustomWhatsThis
		SetFont                         = Qt.WA_SetFont
		NoChildEventsForParent          = Qt.WA_NoChildEventsForParent
		AlwaysShowToolTips              = Qt.WA_AlwaysShowToolTips
		MacBrushedMetal                 = Qt.WA_MacBrushedMetal
		AcceptTouchEvents               = Qt.WA_AcceptTouchEvents
		X11NetWmWindowTypeUtility       = Qt.WA_X11NetWmWindowTypeUtility
		Hover                           = Qt.WA_Hover
		TransparentForMouseEvents       = Qt.WA_TransparentForMouseEvents
		PendingUpdate                   = Qt.WA_PendingUpdate
		PaintUnclipped                  = Qt.WA_PaintUnclipped
		MacMiniSize                     = Qt.WA_MacMiniSize
		MacOpaqueSizeGrip               = Qt.WA_MacOpaqueSizeGrip
		X11NetWmWindowTypeDropDownMenu  = Qt.WA_X11NetWmWindowTypeDropDownMenu
		SetLayoutDirection              = Qt.WA_SetLayoutDirection
		NoMousePropagation              = Qt.WA_NoMousePropagation
		SetLocale                       = Qt.WA_SetLocale
		QuitOnClose                     = Qt.WA_QuitOnClose
		MacSmallSize                    = Qt.WA_MacSmallSize
		MSWindowsUseDirect3D            = Qt.WA_MSWindowsUseDirect3D
		TouchPadAcceptSingleTouchEvents = Qt.WA_TouchPadAcceptSingleTouchEvents
		WState_Reparented               = Qt.WA_WState_Reparented
		ForceUpdatesDisabled            = Qt.WA_ForceUpdatesDisabled
		X11NetWmWindowTypeDND           = Qt.WA_X11NetWmWindowTypeDND
		MacVariableSize                 = Qt.WA_MacVariableSize
		LayoutUsesWidgetRect            = Qt.WA_LayoutUsesWidgetRect
		SetStyle                        = Qt.WA_SetStyle
		WState_ConfigPending            = Qt.WA_WState_ConfigPending
		X11NetWmWindowTypeDesktop       = Qt.WA_X11NetWmWindowTypeDesktop
		X11NetWmWindowTypeMenu          = Qt.WA_X11NetWmWindowTypeMenu
		MacShowFocusRect                = Qt.WA_MacShowFocusRect
		NoMouseReplay                   = Qt.WA_NoMouseReplay
		X11NetWmWindowTypeDock          = Qt.WA_X11NetWmWindowTypeDock
		SetPalette                      = Qt.WA_SetPalette
		OpaquePaintEvent                = Qt.WA_OpaquePaintEvent
		UpdatesDisabled                 = Qt.WA_UpdatesDisabled
		MouseTracking                   = Qt.WA_MouseTracking
		WState_Created                  = Qt.WA_WState_Created
		NoSystemBackground              = Qt.WA_NoSystemBackground
		Disabled                        = Qt.WA_Disabled
		InvalidSize                     = Qt.WA_InvalidSize
		WState_InPaintEvent             = Qt.WA_WState_InPaintEvent
		MacMetalStyle                   = Qt.WA_MacMetalStyle
		X11NetWmWindowTypePopupMenu     = Qt.WA_X11NetWmWindowTypePopupMenu
		NativeWindow                    = Qt.WA_NativeWindow
		WState_ExplicitShowHide         = Qt.WA_WState_ExplicitShowHide
		OutsideWSRange                  = Qt.WA_OutsideWSRange
		SetCursor                       = Qt.WA_SetCursor
		# MergeSoftkeys                   = Qt.WA_MergeSoftkeys
		SetWindowIcon                   = Qt.WA_SetWindowIcon
		X11DoNotAcceptFocus             = Qt.WA_X11DoNotAcceptFocus
		StyledBackground                = Qt.WA_StyledBackground
		X11NetWmWindowTypeToolBar       = Qt.WA_X11NetWmWindowTypeToolBar
		KeyCompression                  = Qt.WA_KeyCompression
		InputMethodTransparent          = Qt.WA_InputMethodTransparent 
		X11NetWmWindowTypeToolTip       = Qt.WA_X11NetWmWindowTypeToolTip
		X11NetWmWindowTypeSplash        = Qt.WA_X11NetWmWindowTypeSplash
		InputMethodEnabled              = Qt.WA_InputMethodEnabled
		StaticContents                  = Qt.WA_StaticContents
		NoX11EventCompression           = Qt.WA_NoX11EventCompression
		AcceptDrops                     = Qt.WA_AcceptDrops
		TintedBackground                = Qt.WA_TintedBackground
		Mapped                          = Qt.WA_Mapped
		MouseNoMask                     = Qt.WA_MouseNoMask
		TranslucentBackground           = Qt.WA_TranslucentBackground
		KeyboardFocusChange             = Qt.WA_KeyboardFocusChange
		X11NetWmWindowTypeNotification  = Qt.WA_X11NetWmWindowTypeNotification
		LaidOut                         = Qt.WA_LaidOut
		WState_OwnSizePolicy            = Qt.WA_WState_OwnSizePolicy
		MacFrameworkScaled              = Qt.WA_MacFrameworkScaled
		MacNoClickThrough               = Qt.WA_MacNoClickThrough
		X11OpenGLOverlay                = Qt.WA_X11OpenGLOverlay
		AttributeCount                  = Qt.WA_AttributeCount
		PaintOnScreen                   = Qt.WA_PaintOnScreen
		X11NetWmWindowTypeCombo         = Qt.WA_X11NetWmWindowTypeCombo
		PendingResizeEvent              = Qt.WA_PendingResizeEvent
		MacAlwaysShowToolWindow         = Qt.WA_MacAlwaysShowToolWindow
		ShowWithoutActivating           = Qt.WA_ShowWithoutActivating
		# MergeSoftkeysRecursively        = Qt.WA_MergeSoftkeysRecursively
		WState_CompressKeys             = Qt.WA_WState_CompressKeys
		UnderMouse                      = Qt.WA_UnderMouse
		WState_Visible                  = Qt.WA_WState_Visible
		GroupLeader                     = Qt.WA_GroupLeader
		MacNormalSize                   = Qt.WA_MacNormalSize
		LayoutOnEntireRect              = Qt.WA_LayoutOnEntireRect
		DeleteOnClose                   = Qt.WA_DeleteOnClose
		WindowPropagation               = Qt.WA_WindowPropagation
		Moved                           = Qt.WA_Moved
		# PaintOutsidePaintEvent          = Qt.WA_PaintOutsidePaintEvent
		DontCreateNativeAncestors       = Qt.WA_DontCreateNativeAncestors
		Resized                         = Qt.WA_Resized
		PendingMoveEvent                = Qt.WA_PendingMoveEvent
		StyleSheet                      = Qt.WA_StyleSheet
		WState_Hidden                   = Qt.WA_WState_Hidden
		X11NetWmWindowTypeDialog        = Qt.WA_X11NetWmWindowTypeDialog
		ForceDisabled                   = Qt.WA_ForceDisabled
		NoChildEventsFromChildren       = Qt.WA_NoChildEventsFromChildren
		WState_Polished                 = Qt.WA_WState_Polished
		WindowModified                  = Qt.WA_WindowModified
	########################################################################
	class WindowFrameSection:
		TopRightSection    = Qt.TopRightSection
		BottomRightSection = Qt.BottomRightSection
		NoSection          = Qt.NoSection
		TopSection         = Qt.TopSection
		TopLeftSection     = Qt.TopLeftSection
		RightSection       = Qt.RightSection
		BottomLeftSection  = Qt.BottomLeftSection
		TitleBarArea       = Qt.TitleBarArea
		LeftSection        = Qt.LeftSection
		BottomSection      = Qt.BottomSection
	########################################################################
	class WindowState:
		WindowNoState    = Qt.WindowNoState
		WindowFullScreen = Qt.WindowFullScreen
		WindowMaximized  = Qt.WindowMaximized
		WindowActive     = Qt.WindowActive
		WindowMinimized  = Qt.WindowMinimized
	########################################################################
	class WindowType:
		SubWindow                    = Qt.SubWindow
		Sheet                        = Qt.Sheet
		Desktop                      = Qt.Desktop
		WindowType_Mask              = Qt.WindowType_Mask
		WindowShadeButtonHint        = Qt.WindowShadeButtonHint
		Window                       = Qt.Window
		WindowMinimizeButtonHint     = Qt.WindowMinimizeButtonHint
		# WindowSoftkeysVisibleHint    = Qt.WindowSoftkeysVisibleHint
		CustomizeWindowHint          = Qt.CustomizeWindowHint
		#WindowCancelButtonHint       = Qt.WindowCancelButtonHint Does not work in maya 2020
		WindowMaximizeButtonHint     = Qt.WindowMaximizeButtonHint
		Widget                       = Qt.Widget
		Popup                        = Qt.Popup
		WindowStaysOnTopHint         = Qt.WindowStaysOnTopHint
		BypassGraphicsProxyWidget    = Qt.BypassGraphicsProxyWidget
		Tool                         = Qt.Tool
		WindowTitleHint              = Qt.WindowTitleHint
		X11BypassWindowManagerHint   = Qt.X11BypassWindowManagerHint
		MSWindowsFixedSizeDialogHint = Qt.MSWindowsFixedSizeDialogHint
		WindowMinMaxButtonsHint      = Qt.WindowMinMaxButtonsHint
		MacWindowToolBarButtonHint   = Qt.MacWindowToolBarButtonHint
		FramelessWindowHint          = Qt.FramelessWindowHint
		#WindowOkButtonHint           = Qt.WindowOkButtonHint does not work in maya 2020
		MSWindowsOwnDC               = Qt.MSWindowsOwnDC
		WindowCloseButtonHint        = Qt.WindowCloseButtonHint
		Dialog                       = Qt.Dialog
		# WindowSoftkeysRespondHint    = Qt.WindowSoftkeysRespondHint
		WindowSystemMenuHint         = Qt.WindowSystemMenuHint
		ToolTip                      = Qt.ToolTip
		WindowContextHelpButtonHint  = Qt.WindowContextHelpButtonHint
		Drawer                       = Qt.Drawer
		WindowStaysOnBottomHint      = Qt.WindowStaysOnBottomHint
		SplashScreen                 = Qt.SplashScreen
########################################################################
class Standered_Item_Data_Roles(object):
	""""""
	## The general purpose roles (and the associated types):
	DISPLAY        = Qt.DisplayRole       ## The key data to be rendered in the form of text.                                                :: QtCore.QString
	DECORATION     = Qt.DecorationRole    ## The data to be rendered as a decoration in the form of an icon.                                 :: QT.QColor | QT.QIcon | QtGui.QPixmap
	EDIT           = Qt.EditRole          ## The data in a form suitable for editing in an editor.                                           :: QString
	TOOLTIP        = Qt.ToolTipRole       ## The data displayed in the item's tooltip.                                                       :: QtCore.QString
	STATUSTIP      = Qt.StatusTipRole     ## The data displayed in the status bar.                                                           :: QtCore.QString
	WHATSTHIS      = Qt.WhatsThisRole     ## The data displayed for the item in What's This? mode.                                           :: QtCore.QString
	SIZEHINT       = Qt.SizeHintRole      ## The size hint for the item that will be supplied to views.                                      :: QtCore.QSize
	DP_ED          = [DISPLAY,EDIT]

	##Roles describing appearance and meta data (with associated types):

	FONT           = Qt.FontRole          ## The font used for items rendered with the default delegate.                                     :: QtGui.QFont
	TEXT_ALIGNMENT = Qt.TextAlignmentRole ## The alignment of the text for items rendered with the default delegate.                         :: Qt.AlignmentFlag
	BACKGROUND     = Qt.BackgroundRole    ## The background brush used for items rendered with the default delegate.                         :: QtGui.QBrush
	FOREGROUND     = Qt.ForegroundRole    ## The foreground brush (text color, typically) used for items rendered with the default delegate. :: QtGui.QBrush
	CHECKSTATE     = Qt.CheckStateRole    ## This role is used to obtain the checked state of an item.                                       :: Qt.CheckState
########################################################################
class Item_Data_Roles(Standered_Item_Data_Roles):
	""""""
	USER           = QT.userRole_counter()
	ITEM           = QT.userRole_counter()
	#ITEM_DATA      = QT.userRole_counter()
	#TABLE          = QT.userRole_counter()
	#REFS           = QT.userRole_counter()
	#ELEM           = QT.userRole_counter()
	#ELEM_DATA      = QT.userRole_counter()
	#ELEM_TEXT      = QT.userRole_counter()
	#ELEM_ATTR      = QT.userRole_counter()
	#ELEM_ATTR_VALUE= QT.userRole_counter()
	#ELEM_ATTR_TYPE = QT.userRole_counter()
	#EDIT_UNDO      = QT.userRole_counter()
########################################################################
class PenStyles:
	NoPen          = Qt.NoPen          # no line at all. For example, QPainter.drawRect() fills but does not draw any boundary line.
	SolidLine      = Qt.SolidLine      # A plain line.
	DashLine       = Qt.DashLine       # Dashes separated by a few pixels.
	DotLine        = Qt.DotLine        # Dots separated by a few pixels.
	DashDotLine    = Qt.DashDotLine    # Alternate dots and dashes.
	DashDotDotLine = Qt.DashDotDotLine # One dash, two dots, one dash, two dots.
	CustomDashLine = Qt.CustomDashLine # A custom pattern defined using QPainterPathStroker.setDashPattern() .
########################################################################
class BrushStyles:
	NoBrush                = Qt.NoBrush                # No brush pattern.
	SolidPattern           = Qt.SolidPattern           # Uniform color.
	Dense1Pattern          = Qt.Dense1Pattern          # Extremely dense brush pattern.
	Dense2Pattern          = Qt.Dense2Pattern          # Very dense brush pattern.
	Dense3Pattern          = Qt.Dense3Pattern          # Somewhat dense brush pattern.
	Dense4Pattern          = Qt.Dense4Pattern          # Half dense brush pattern.
	Dense5Pattern          = Qt.Dense5Pattern          # Somewhat sparse brush pattern.
	Dense6Pattern          = Qt.Dense6Pattern          # Very sparse brush pattern.
	Dense7Pattern          = Qt.Dense7Pattern          # Extremely sparse brush pattern.
	HorPattern             = Qt.HorPattern             # Horizontal lines.
	VerPattern             = Qt.VerPattern             # Vertical lines.
	CrossPattern           = Qt.CrossPattern           # Crossing horizontal and vertical lines.
	BDiagPattern           = Qt.BDiagPattern           # Backward diagonal lines.
	FDiagPattern           = Qt.FDiagPattern           # Forward diagonal lines.
	DiagCrossPattern       = Qt.DiagCrossPattern       # Crossing diagonal lines.
	LinearGradientPattern  = Qt.LinearGradientPattern  # Linear gradient (set using a dedicated PySide.QtGui.QBrush constructor).
	ConicalGradientPattern = Qt.ConicalGradientPattern # Conical gradient (set using a dedicated PySide.QtGui.QBrush constructor).
	RadialGradientPattern  = Qt.RadialGradientPattern  # Radial gradient (set using a dedicated PySide.QtGui.QBrush constructor).
	TexturePattern         = Qt.TexturePattern         # Custom pattern (see QBrush.setTexture() ).
########################################################################
class DropActions:
	CopyAction       = Qt.CopyAction       # Copy the data to the target.
	MoveAction       = Qt.MoveAction       # Move the data from the source to the target.
	LinkAction       = Qt.LinkAction       # Create a link from the source to the target.
	ActionMask       = Qt.ActionMask       #
	IgnoreAction     = Qt.IgnoreAction     # Ignore the action (do nothing with the data).
	TargetMoveAction = Qt.TargetMoveAction # On Windows, this value is used when the ownership of the D&D data should be taken over by the target application, i.e., the source application should not delete the data. .. raw:: html <br /> On X11 this value is used to do a move. .. raw:: html <br /> TargetMoveAction is not used on the Mac.
########################################################################
class GestureTypes:
	TapGesture          = Qt.TapGesture           # A Tap gesture.
	TapAndHoldGesture   = Qt.TapAndHoldGesture    # A Tap-And-Hold (Long-Tap) gesture.
	PanGesture          = Qt.PanGesture           # A Pan gesture.
	PinchGesture        = Qt.PinchGesture         # A Pinch gesture.
	SwipeGesture        = Qt.SwipeGesture         # A Swipe gesture.
	CustomGesture       = Qt.CustomGesture        # A flag that can be used to test if the gesture is a user-defined gesture ID.
########################################################################
class CheckStates:
	Unchecked          = Qt.Unchecked           # The item is unchecked.
	PartiallyChecked   = Qt.PartiallyChecked    # The item is partially checked. Items in hierarchical models may be partially checked if some, but not all, of their children are checked
	Checked            = Qt.Checked             # The item is checked.
########################################################################
class ItemFlag:
	NoItemFlags           = Qt.NoItemFlags         # It does not have any properties set.
	IsSelectable          = Qt.ItemIsSelectable    # It can be selected.
	IsEditable            = Qt.ItemIsEditable      # It can be edited.
	IsDragEnabled         = Qt.ItemIsDragEnabled   # It can be dragged.
	IsDropEnabled         = Qt.ItemIsDropEnabled   # It can be used as a drop target.
	IsUserCheckable       = Qt.ItemIsUserCheckable # It can be checked or unchecked by the user.
	IsEnabled             = Qt.ItemIsEnabled       # The user can interact with the item.
	IsTristate            = Qt.ItemIsTristate      # The item is checkable with three separate states.
########################################################################
class AlignmentFlag:	
	Absolute        = Qt.AlignAbsolute
	Bottom          = Qt.AlignBottom
	Center          = Qt.AlignCenter
	HCenter         = Qt.AlignHCenter
	Horizontal_Mask = Qt.AlignHorizontal_Mask
	Justify         = Qt.AlignJustify
	Leading         = Qt.AlignLeading
	Left            = Qt.AlignLeft
	Right           = Qt.AlignRight
	Top             = Qt.AlignTop
	Trailing        = Qt.AlignTrailing
	VCenter         = Qt.AlignVCenter
	Vertical_Mask   = Qt.AlignVertical_Mask
########################################################################
class MatchFlag:

	CaseSensitive = Qt.MatchCaseSensitive
	Contains      = Qt.MatchContains
	EndsWith      = Qt.MatchEndsWith
	Exactly       = Qt.MatchExactly
	FixedString   = Qt.MatchFixedString
	Recursive     = Qt.MatchRecursive
	RegExp        = Qt.MatchRegExp
	StartsWith    = Qt.MatchStartsWith
	Wildcard      = Qt.MatchWildcard
	Wrap          = Qt.MatchWrap
########################################################################
class DayOfWeek:
	Friday    = Qt.Friday
	Monday    = Qt.Monday
	Saturday  = Qt.Saturday
	Sunday    = Qt.Sunday
	Thursday  = Qt.Thursday
	Tuesday   = Qt.Tuesday
	Wednesday = Qt.Wednesday
########################################################################
class MouseButton:
	RightButton     = Qt.RightButton
	MiddleButton    = Qt.MiddleButton
	NoButton        = Qt.NoButton
	LeftButton      = Qt.LeftButton
	MouseButtonMask = Qt.MouseButtonMask
	XButton1        = Qt.XButton1
	XButton2        = Qt.XButton2
	MidButton       = Qt.MidButton
########################################################################
class Modifier:
	CTRL          = Qt.CTRL
	SHIFT         = Qt.SHIFT
	UNICODE_ACCEL = Qt.UNICODE_ACCEL
	MODIFIER_MASK = Qt.MODIFIER_MASK
	META          = Qt.META
	ALT           = Qt.ALT
########################################################################	
class SizeHint:
	MinimumDescent = Qt.MinimumDescent
	PreferredSize  = Qt.PreferredSize
	MinimumSize    = Qt.MinimumSize
	MaximumSize    = Qt.MaximumSize
########################################################################	
class TextFlag:
	TextShowMnemonic          = Qt.TextShowMnemonic
	TextHideMnemonic          = Qt.TextHideMnemonic
	TextJustificationForced   = Qt.TextJustificationForced
	TextDontClip              = Qt.TextDontClip
	TextIncludeTrailingSpaces = Qt.TextIncludeTrailingSpaces
	TextDontPrint             = Qt.TextDontPrint
	TextSingleLine            = Qt.TextSingleLine
	TextWrapAnywhere          = Qt.TextWrapAnywhere
	TextExpandTabs            = Qt.TextExpandTabs
	TextWordWrap              = Qt.TextWordWrap

class File_Dialog_Options:
	ShowDirsOnly          = QT.QFileDialog.ShowDirsOnly          # Only show directories in the file dialog. By default both files and directories are shown. (Valid only in the Directory file mode.)
	DontResolveSymlinks   = QT.QFileDialog.DontResolveSymlinks   # Don't resolve symlinks in the file dialog. By default symlinks are resolved.
	DontConfirmOverwrite  = QT.QFileDialog.DontConfirmOverwrite  # Don't ask for confirmation if an existing file is selected. By default confirmation is requested.
	DontUseNativeDialog   = QT.QFileDialog.DontUseNativeDialog   # Don't use the native file dialog. By default, the native file dialog is used unless you use a subclass of PySide.QT.QFileDialog that contains the Q_OBJECT() macro.
	ReadOnly              = QT.QFileDialog.ReadOnly              # Indicates that the model is readonly.
	HideNameFilterDetails = QT.QFileDialog.HideNameFilterDetails # Indicates if the file name filter details are hidden or not.
	DontUseSheet          = QT.QFileDialog.DontUseSheet          # In previous versions of Qt, the static functions would create a sheet by default if the static function was given a parent. This is no longer supported and does nothing in Qt 4.5, The static functions will always be an application modal dialog. If you want to use sheets, use QFileDialog.open() instead.
