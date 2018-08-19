import os, xbmc, xbmcaddon

#########################################################
### User Edit Variables #################################
#########################################################
ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = 'Looking Glass Wizard'
EXCLUDES       = [ADDON_ID]
# Text File with build info in it.
BUILDFILE      = 'http://www.tvandroidianox.com/Wizard2/wizard.txt'
# How often you would like it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK    = 0
# Text File with APK info in it.
APKFILE        = 'http://www.lookingglass.rocks/xmls/LookingGlassApks.txt'
# Text File with Youtube Videos URLs.  Leave as 'http://' to ignore
YOUTUBETITLE   = 'Video y Guias de la instalacion'
YOUTUBEFILE    = 'http://tvandroidianox.com/Wizard/Video%20Guias%20VipTV0.txt'
# Text File for addon installer.  Leave as 'http://' to ignore
ADDONFILE      = 'http://tvandroidianox.com/Addon/'
# Text File for advanced settings.  Leave as 'http://' to ignore
ADVANCEDFILE   = 'http://'

# Dont need to edit just here for icons stored locally
PATH           = xbmcaddon.Addon().getAddonInfo('path')
ART            = os.path.join(PATH, 'resources', 'art')

#########################################################
### THEMING MENU ITEMS ##################################
#########################################################
# If you want to use locally stored icons then place them in the Resources/Art/
# folder of the Wizard then use os.path.join(ART, 'imagename.png')
# Do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'http://aftermathwizard.net/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONBUILDS     = 'http://tvandroidianox.com/Wizard2/icon%20Instalar%20y%20Actualizar%20VipTV.jpg'
ICONMAINT      = 'http://tvandroidianox.com/Wizard/icono%20de%20mantenimiento%20viptv.png'
ICONAPK        = 'http://www.lookingglass.rocks/images/forks.jpg'
ICONADDONS     = 'http://tvandroidianox.com/Wizard/Icon%20addon%20viptv%20descaga.png'
ICONYOUTUBE    = 'http://tvandroidianox.com/Wizard/icon%20viptv%20videos%20guias%20y%20tutoriales.png'
ICONSAVE       = 'http://tvandroidianox.com/Wizard/icon%20save%20viptv.png'
ICONTRAKT      = 'http://tvandroidianox.com/Wizard/publicidad.jpg'
ICONREAL       = 'http://tvandroidianox.com/Wizard/publicidad.jpg'
ICONLOGIN      = 'http://www.lookingglass.rocks/images/login.jpg'
ICONCONTACT    = 'http://tvandroidianox.com/Wizard/AlexisTV.png'
ICONSETTINGS   = 'http://tvandroidianox.com/Wizard/ajustes.png'
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'No'
# Character used in seperator
SPACER         = '*-'

# You can edit these however you want, just make sure that you have a %s in each of the
# THEMEs so it grabs the text from the menu item
COLOR1         = 'magenta'
COLOR2         = 'cyan'
# Primary Menu Items   / %s is the menu item and is required
THEME1         = '[COLOR '+COLOR1+'][I][B]([COLOR '+COLOR2+']VipTV[/COLOR])[/B][/I][/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR2+']%s[/COLOR]'
# Alternate Items      / %s is the menu item and is required
THEME3         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Current Build Header / %s is the menu item and is required
THEME4         = '[COLOR '+COLOR1+']Current Build:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
# Chosen Build Header / %s is the menu item and is required
THEME5         = '[COLOR '+COLOR1+']Chosen Build:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
# Current Theme Header / %s is the menu item and is required
THEME6         = '[COLOR '+COLOR1+']Current Theme:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' don't hide
HIDECONTACT    = 'No'
# You can add \n to do line breaks
CONTACT        = '[B][COLOR '+COLOR2+']Para adquirir VipTV Wizard escribeme por Whatsapp AlexisTV o twitter[COLOR '+COLOR1+']@Tvandroidian0x[/COLOR]. Gracias por preferir VipTV Wizard[COLOR '+COLOR1+']en conjunto con Tvandroidiano [/COLOR] Team\'s Wizard!\r\n\r\nPara Preguntas/o respuestas contactame a mi numero:  [COLOR '+COLOR1+']AlexisTV[/COLOR][/B]'
#Images used for the contact window.  http:// for default icon and fanart
CONTACTICON    = 'http://'
CONTACTFANART  = ''
#########################################################

#########################################################
### AUTO UPDATE #########################################
########## FOR THOSE WITH NO REPO #######################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'No'
# URL to wizard version
WIZARDFILE     = 'http://tvandroidianox.com/Wizard/Wizard%20VipTV.txt'
#########################################################

#########################################################
### AUTO INSTALL REPO ###################################
############### IF NOT INSTALLED ########################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL    = 'No'
# Addon ID for the repository
REPOID         = ''
# URL to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = ''
# URL to folder zip is located in
REPOZIPURL     = ''
#########################################################

#########################################################
### NOTIFICATION WINDOW #################################
#########################################################
# Enable Notification screen Yes or No
ENABLE         = 'No'
# URL to notification file
NOTIFICATION   = ''
# Use either 'Text' or 'Image'
HEADERTYPE     = 'Text'
HEADERMESSAGE  = '[B]VipTV Wizard[/B]'
# URL to image if using Image 424x180
HEADERIMAGE    = ''
# Background for Notification Window
BACKGROUND     = ''
#########################################################