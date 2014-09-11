"""
Solves the given vignere cipher
"""

__author__ = 'Michael'

num_bins = 5

cipher_text = 'gbrowlkbbiahvsywlclfjsesyadftyshiaeagueuabghvsfptzuabrvlvnnffsuuevfrdrfrfiolmlerjgngfzofbvwbsolfrpaesrnsgjwzedabvskwffapkggegzsahrjdrrjswqikoofueuzraiovvcykvvpysroevftbuevphtgzcgovnwqeeuspoexwemvvwgwrkcaefxhuedkwejfzbsrrfyyiedsqtywhjojzwcsrfrbnvziadiwrnnulkrnkqbvnvesaiewwthkwsaffjhlfznsgotzoetkzsaoilvjejldnsjsurielvrcrfoqirfoeckaqghvwlceuahvoekrvsrhdraisbpejzcetcqostvjprcresbnvgtghvyfrakemftvjwrsfxhuerysbfmaqgoiaoaeohzbrrlwbnkzspaesrvaeycieifarnktstaeksnrtzwagwgfsrrfyyiekguigkwatnghuolkoadrfrrixzhnsgsfgowsggrrlstykgofsvjhpaesrnsjgjrrvauatpgjrrkzsaoilvjejldnsjsurwyaquhrkfrcvfhyyswqbmvsqpejkwolvlcfhzhdvnxtspalksbfdwzgieyoeckaqvcvwlceuahvoekcaaiaangvkteodlvrwrlsesfxjvckgfvajlfnikbiftfxtxieykvlcaozijdoadtdsnrcqguonlvrwiwqxaxwcsajzwcoelvrotwoafcgceirerrlzyvgeulcnnegiacvlvntkzwfyvsffvzuhbrzsggrrahrxgwrvtzgbuajkcyvvvcaefxqnnrvofgiwogejlalskwfvejowghkzsqijucieiqcsoewcstywhjojzwcsswzbnxabttflvrfisbxlzfskpvvwgiffdeidwavnzkhrrjlschvfvnrgwffazvwaajlogedwbgfzfrvnxlvrfzjggvvkgrlnazynfvchbkhfbvzvsghveczeelizoiowadzfchrjswysewqrsjsfltfdcpakwwgsjaggeikvvprfrsievchtvnsamfjsnbfmhjhrlvnpgwbrdkghuewjoakcabrxgwrvtzgbfciwkghvxwadysgoevfrrstjwoeusgghvtwtgvkhnrtzorocguvcrdrvstgjrrplvrwfjzqhrkgreekwacvlvrogwbvnxgtguksbxhreiaskgaoacecftffsuuevfrdpwoesrycoyrtfvtzkvnrtzorocguvskowylzsaoaklsessqkuoysgjrzlhrnvphrnjajrlpspbuklvrfisbxlzfskpvvwgiffteodlvridsurszlwfccwoetyshnhlysnmfmbgowwjvdvfqrwzdzoegjsfeinsqfigaghvwlceuahvoehcfsztzlemwbvntdiqieyhueiwaniekcstywarnrfrzaptswujldbsjapyyjgarowlvriihvbtfyfnpykvrsrarghvdcfsfxvzsvjsoujsbqhdkhrrigfjhzuvjajtivlkabgogkvnmuwjbngjczpkwrbnvgtyaiysftjwoecywgvnyaggoiqfhneabtfigarixzhreexcetpwwthklcrixzhreexwstpfwaekzszyjlseyysgtrzhdrdgwcclvxcegvfseakacaszfdnrktspalksaoffsxnfogsoikieevpoptcqkuakzocpvfsqtflvrciwkrxgwfgsswzvemwhuejzwcsnwfrlfkhjhvfhueptspadwzbcbwrvnkzsvcvfsnrbabtwzdzvadagyaevoadkzogtywqeenkooaevcaeulvrmzfouogwzrsjtwqtfjsncykosekqfrpfjhfaklvrtzessrfezbcrdwauzlgfaplvrmvfrrsgwfntvxceffgreejgfgeulcpaefwoacagzbvxceekzsldzwrfiibcunwjoakcabfwzxsfpvsfuervsqaeshgedhhgowabqhzeznueuvvnxxwiejzwcszfgraiuvbfywfuujtoadrfrrvvfzramabtcrfgbfwgcqoelvritwwatywrrsgwfntvzcceywkbucvtvnulvrmzfhbtrdabrvlvnnwatgyvpdrdzlwbnjbcvnvvhuejwoecylveevtcqivkrvstgjrrvvcieisqrnkmfllrlseielvrnzfsgevfsvgylmfwvjssolfrgoysjrayauulvsrpoelsatrfrgokzwfdrqannphsbpcwprlzwjrtywcaeymbqrvvoadkosatpfwaetjsjmveprrjoseeggwfoewroycwoxieyzrauabghvafcofjzlsfdrrrvvhvntsbfmfjseetwbgrvksnrtzghgxwggskzspaefsqffgrfughzveulcsrrfyyieoofnflopiuaqrnfmuuffjhuaklcuaghsaaevhuecwoqwrkabrvdwxecqhbhrnspodwteodlvrielsenrddvpvkmftvecatywguigkhuejwoecyjsfuclsqielvrdzkqbvvjmbfkzsaoilvjejldnsjsurwyaqurlfgsrfehuerlznnkaqgokzscatatvckzfbuxzhuerjqgitsfphzhsyaxghueuagpomwflowxfnnbdwasmwgfeckwfcffgvdvjsqoewcstywabskkchgylostvjdeiqwgvndsfvnvsfphrwcyoxqogerecscrfoqirfrvvvjgnnusfphrwcyoxaggsysgoevfheyzfugowabqtywguigkgvntwhjokzchsrfrnnuwwthk'

ord_a = ord('a')
ord_e = ord('e')
ord_z = ord('z')

def generate_bins():
    """
    Breaks input into bins
    :return: list of bins with the input
    """
    #initialize bins
    bins = []
    for i in range(num_bins):
        bins.append([])
    #fill in bins
    bin_number = 0
    for c in cipher_text:
        #adjust bin number
        if bin_number >= num_bins:
            bin_number = 0
        bins[bin_number].append(c)
        bin_number += 1
    return bins


def calculate_stats(bins):
    """
    Calculates the Index of Coincidence per bin
    :param bins:
    :return:
    """
    shifted_bins = []
    for index, bin in enumerate(bins):
        #build up the frequency map for the letters in the bin
        freq_map = {}
        for c in bin:
            if not c in freq_map:
                freq_map[c] = 0
            freq_map[c] += 1
        # calculate the ic for this bin
        numerator = 0
        for key in freq_map.keys():
            numerator += freq_map[key] * (freq_map[key] - 1)
        n = float(len(bin))
        denominator = n * (n-1)
        ic = numerator / denominator
        print "IC for bin #%s is %s" % (index, ic)
        #find the letter with the highest frequency
        sorted_tuples = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)
        print("SORTED KEY, VALUES: " + str(sorted_tuples))
        highest_key = sorted_tuples[0][0]
        print("HIGHEST KEY: %s" % highest_key)
        ord_diff = ord(highest_key) - ord_e
        #adjust for left shifts
        if ord_diff < 0:
            ord_diff = 26 + -1 * ord_diff
        print "Shift by " + str(ord_diff)
        updated_bin = rotate_letters(bin, ord_diff)
        shifted_bins.append(updated_bin)
    #print the plaintext
    chr_index = 0
    plaintext = ''
    while True:
        should_stop = False
        for bin_index in range(len(shifted_bins)):
            continue_with_loop = chr_index < len(shifted_bins[bin_index])
            should_stop = should_stop or not continue_with_loop
            if continue_with_loop:
                plaintext += shifted_bins[bin_index][chr_index]
        if should_stop:
            break
        chr_index += 1
    #print the plaintext
    print plaintext


def rotate_letters(bin, ordinal):
    """
    Rotate all of the letters in the bin by the ordinal
    :param bin: The list of characters
    :param ordinal: The ordinal difference to shift left by
    :return: An updated bin
    """
    print "Original bin: " + str(bin)
    updated_bin = []
    adjusted_ordinal = 26 - ordinal
    print "Adjusted Ordinal: %d\n" % adjusted_ordinal
    for c in bin:
        ordinal_c = ord(c) + adjusted_ordinal
        diff_z = ordinal_c - ord_z
        #adjust for ordinals above z
        if diff_z > 0:
            ordinal_c = ord_a + diff_z - 1
        new_char = chr(ordinal_c)
        updated_bin.append(new_char)
    print "Updated bin: " + str(updated_bin)
    return updated_bin

def main():
    bins = generate_bins()
    for bin in bins:
        print "%s\n" % bin
    calculate_stats(bins)


if __name__ == '__main__':
    main()