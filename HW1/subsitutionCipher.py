__author__ = 'Michael Trotter (trotsky@gwu.edu)'

text = "theshadowofthemoonsweptacrosstheglobefromhongkongtothetexaspanhandleasarareannularsolareclipsebeganmondaymorninginasiaandtraversedthepacificthesunappearedasathinringbehindthemoontopeopleinanarrowpathalongthecenterofthetrackwhichbeganinsouthernchinaheavycloudsobscuredtheviewinhongkongbutresidentsoftokyoandothercitieswereabletogetaspectacularviewforaboutfourminutesaroundseventhirtytwoammondaysixthirtytwopmetsundayeventswereheldatschoolsandmuseumsinjapanwhilemanymorepeopletookintheunusualastronomicaleventathomeoronstreetcornersafterwhizzingacrossthepacifictheshadowemergedovernortherncaliforniaandsouthernoregonwherethousandsofpeopleattendedpartiestowatchtheeventthefirsttoappearintheunitedstatessincenineteenninetyfourexpertswarnedthathopefulviewersshouldnotpeerupattheskywithoutspecialviewingequipmentsincelookingatthesunwiththenakedeyecancauseblindnessderekralstonaprofessionalphotographersaidheusedaweldingfiltertocaptureadirectviewofeclipseinthefoothillsaboveorovillecaliforniahesharedthephotooncnnireportnotingtheratherslimswathoftheglobewhocouldseetheimpactoftheeclipseralstonsaidhewantedtoenabletherestoftheworldtoseehowclearitlookedtothoseofuswhowerefortunateenoughtoseeitthesliverofsunshinethentraveledsoutheastacrosscentralnevadasouthernutahandnorthernarizonaandthennewmexicoitpassedoveralbuquerquenewmexicoaboutseventhirtyfourpmninethirtyfourpmetbeforepeteringouteastoflubbocktexasaccordingtonasa"

cipher_text = ""

frequency_table = {
    'a': 'e',
    'b': 'j',
    'c': 'g',
    'd': 'i',
    'e': 'q',
    'f': 'k',
    'g': 'v',
    'h': 'c',
    'i': 'l',
    'j': 'h',
    'k': 'n',
    'l': 'p',
    'm': 'r',
    'n': 'b',
    'o': 's',
    'p': 'u',
    'q': 'x',
    'r': 'w',
    's': 'y',
    't': 'a',
    'u': 'f',
    'v': 'm',
    'w': 'o',
    'x': 'z',
    'y': 't',
    'z': 'd'
}

for c in text:
    cipher_text += frequency_table[c]

print cipher_text