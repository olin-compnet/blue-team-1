﻿import random
def quote():
    return makeMorseHappy(quotes[randon.randint(0,len(quotes))])

def makeMorsehappy(Q):
	return "".join([a if a in string.ascii_uppercase+" " else " "+"".join(unicodedata.name(a,"").split("-"))+" " for a in Q.upper() ])






quotes=[
   '''** START OF THIS PROJECT GUTENBERG EBOOK MOBY DICK; OR THE WHALE ***
''',







"""The pale Usher--threadbare in coat, heart, body, and brain; I see him
now. He was ever dusting his old lexicons and grammars, with a queer
handkerchief, mockingly embellished with all the gay flags of all
the known nations of the world. He loved to dust his old grammars; it
somehow mildly reminded him of his mortality.""",

'''"While you take in hand to school others, and to teach them by what
name a whale-fish is to be called in our tongue leaving out, through
ignorance, the letter H, which almost alone maketh the signification of
the word, you deliver that which is not true." --HACKLUYT''',

'''"WHALE.... Sw. and Dan. HVAL. This animal is named from roundness or
rolling; for in Dan. HVALT is arched or vaulted." --WEBSTER'S DICTIONARY'''
,
'''"WHALE.... It is more immediately from the Dut. and Ger. WALLEN; A.S.
WALW-IAN, to roll, to wallow." --RICHARDSON'S DICTIONARY

     KETOS,               GREEK.
     CETUS,               LATIN.
     WHOEL,               ANGLO-SAXON.
     HVALT,               DANISH.
     WAL,                 DUTCH.
     HWAL,                SWEDISH.
     WHALE,               ICELANDIC.
     WHALE,               ENGLISH.
     BALEINE,             FRENCH.
     BALLENA,             SPANISH.
     PEKEE-NUEE-NUEE,     FEGEE.
     PEHEE-NUEE-NUEE,     ERROMANGOAN.
'''

,


'''EXTRACTS (Supplied by a Sub-Sub-Librarian).

It will be seen that this mere painstaking burrower and grub-worm of a
poor devil of a Sub-Sub appears to have gone through the long Vaticans
and street-stalls of the earth, picking up whatever random allusions to
whales he could anyways find in any book whatsoever, sacred or
profane. Therefore you must not, in every case at least, take the
higgledy-piggledy whale statements, however authentic, in these
extracts, for veritable gospel cetology. Far from it. As touching the
ancient authors generally, as well as the poets here appearing, these
extracts are solely valuable or entertaining, as affording a glancing
bird's eye view of what has been promiscuously said, thought, fancied,
and sung of Leviathan, by many nations and generations, including our
own.

So fare thee well, poor devil of a Sub-Sub, whose commentator I am. Thou
belongest to that hopeless, sallow tribe which no wine of this world
will ever warm; and for whom even Pale Sherry would be too rosy-strong;
but with whom one sometimes loves to sit, and feel poor-devilish, too;
and grow convivial upon tears; and say to them bluntly, with full eyes
and empty glasses, and in not altogether unpleasant sadness--Give it up,
Sub-Subs! For by how much the more pains ye take to please the world,
by so much the more shall ye for ever go thankless! Would that I could
clear out Hampton Court and the Tuileries for ye! But gulp down your
tears and hie aloft to the royal-mast with your hearts; for your friends
who have gone before are clearing out the seven-storied heavens, and
making refugees of long-pampered Gabriel, Michael, and Raphael, against
your coming. Here ye strike but splintered hearts together--there, ye
shall strike unsplinterable glasses!  Herman Melville from Moby Dick.
'''
   ,

'''"And God created great whales." --GENESIS.'''
,
'''"Leviathan maketh a path to shine after him; One would think the deep to
be hoary." --JOB.'''
,
'''"Now the Lord had prepared a great fish to swallow up Jonah." --JONAH.'''




,
















'''"There go the ships; there is that Leviathan whom thou hast made to play
therein." --PSALMS.'''
,
'''"In that day, the Lord with his sore, and great, and strong sword,
shall punish Leviathan the piercing serpent, even Leviathan that crooked
serpent; and he shall slay the dragon that is in the sea." --ISAIAH'''
,
'''"And what thing soever besides cometh within the chaos of this monster's
mouth, be it beast, boat, or stone, down it goes all incontinently that
foul great swallow of his, and perisheth in the bottomless gulf of his
paunch." --HOLLAND'S PLUTARCH'S MORALS.'''
,
'''"The Indian Sea breedeth the most and the biggest fishes that are: among
which the Whales and Whirlpooles called Balaene, take up as much in
length as four acres or arpens of land." --HOLLAND'S PLINY.
''',
'''"Scarcely had we proceeded two days on the sea, when about sunrise a
great many Whales and other monsters of the sea, appeared. Among the
former, one was of a most monstrous size.... This came towards us,
open-mouthed, raising the waves on all sides, and beating the sea before
him into a foam." --TOOKE'S LUCIAN. "THE TRUE HISTORY."'''
,
'''"He visited this country also with a view of catching horse-whales,
which had bones of very great value for their teeth, of which he brought
some to the king.... The best whales were catched in his own country, of
which some were forty-eight, some fifty yards long. He said that he was
one of six who had killed sixty in two days." --OTHER OR OTHER'S VERBAL
NARRATIVE TAKEN DOWN FROM HIS MOUTH BY KING ALFRED, A.D. 890.'''
,
'''"And whereas all the other things, whether beast or vessel, that
enter into the dreadful gulf of this monster's (whale's) mouth, are
immediately lost and swallowed up, the sea-gudgeon retires into it in
great security, and there sleeps." --MONTAIGNE. --APOLOGY FOR RAIMOND
SEBOND.'''
,
'''"Let us fly, let us fly! Old Nick take me if is not Leviathan described
by the noble prophet Moses in the life of patient Job." --RABELAIS.'''

'''"This whale's liver was two cartloads." --STOWE'S ANNALS.'''
,
'''"The great Leviathan that maketh the seas to seethe like boiling pan."
--LORD BACON'S VERSION OF THE PSALMS.
''',
'''"Touching that monstrous bulk of the whale or ork we have received
nothing certain. They grow exceeding fat, insomuch that an incredible
quantity of oil will be extracted out of one whale." --IBID. "HISTORY OF
LIFE AND DEATH."'''
,
'''"The sovereignest thing on earth is parmacetti for an inward bruise."
--KING HENRY.
'''
   ,
'''"Very like a whale." --HAMLET.'''
,
'''     "Which to secure, no skill of leach's art
     Mote him availle, but to returne againe
     To his wound's worker, that with lowly dart,
     Dinting his breast, had bred his restless paine,
     Like as the wounded whale to shore flies thro' the maine."
     --THE FAERIE QUEEN.
''',
'''"Immense as whales, the motion of whose vast bodies can in a peaceful
calm trouble the ocean til it boil." --SIR WILLIAM DAVENANT. PREFACE TO
GONDIBERT.
''',
'''"What spermacetti is, men might justly doubt, since the learned
Hosmannus in his work of thirty years, saith plainly, Nescio quid sit."
--SIR T. BROWNE. OF SPERMA CETI AND THE SPERMA CETI WHALE. VIDE HIS V.
E.''',

     '''"Like Spencer's Talus with his modern flail
     He threatens ruin with his ponderous tail.
   ...
     Their fixed jav'lins in his side he wears,
     And on his back a grove of pikes appears."
     --WALLER'S BATTLE OF THE SUMMER ISLANDS.
''',
'''"By art is created that great Leviathan, called a Commonwealth or
State--(in Latin, Civitas) which is but an artificial man." --OPENING
SENTENCE OF HOBBES'S LEVIATHAN.
''',
'''"Silly Mansoul swallowed it without chewing, as if it had been a sprat
in the mouth of a whale." --PILGRIM'S PROGRESS.
''',
   '''  "That sea beast
     Leviathan, which God of all his works
     Created hugest that swim the ocean stream." --PARADISE LOST.
''',
   '''  ---"There Leviathan,
     Hugest of living creatures, in the deep
     Stretched like a promontory sleeps or swims,
     And seems a moving land; and at his gills
     Draws in, and at his breath spouts out a sea." --IBID.
''',
'''"The mighty whales which swim in a sea of water, and have a sea of oil
swimming in them." --FULLLER'S PROFANE AND HOLY STATE.
''',
   '''  "So close behind some promontory lie
     The huge Leviathan to attend their prey,
     And give no chance, but swallow in the fry,
     Which through their gaping jaws mistake the way."
     --DRYDEN'S ANNUS MIRABILIS.
''',
'''"While the whale is floating at the stern of the ship, they cut off his
head, and tow it with a boat as near the shore as it will come; but it
will be aground in twelve or thirteen feet water." --THOMAS EDGE'S TEN
VOYAGES TO SPITZBERGEN, IN PURCHAS.
''',
'''"In their way they saw many whales sporting in the ocean, and in
wantonness fuzzing up the water through their pipes and vents, which
nature has placed on their shoulders." --SIR T. HERBERT'S VOYAGES INTO
ASIA AND AFRICA. HARRIS COLL.
''',
'''"Here they saw such huge troops of whales, that they were forced to
proceed with a great deal of caution for fear they should run their ship
upon them." --SCHOUTEN'S SIXTH CIRCUMNAVIGATION.
''',
'''"We set sail from the Elbe, wind N.E. in the ship called The
Jonas-in-the-Whale.... Some say the whale can't open his mouth, but that
is a fable.... They frequently climb up the masts to see whether they
can see a whale, for the first discoverer has a ducat for his pains....
I was told of a whale taken near Shetland, that had above a barrel of
herrings in his belly.... One of our harpooneers told me that he caught
once a whale in Spitzbergen that was white all over." --A VOYAGE TO
GREENLAND, A.D. 1671 HARRIS COLL.
''',
'''"Several whales have come in upon this coast (Fife) Anno 1652, one
eighty feet in length of the whale-bone kind came in, which (as I was
informed), besides a vast quantity of oil, did afford 500 weight of
baleen. The jaws of it stand for a gate in the garden of Pitferren."
--SIBBALD'S FIFE AND KINROSS.
''',
'''"Myself have agreed to try whether I can master and kill this
Sperma-ceti whale, for I could never hear of any of that sort that was
killed by any man, such is his fierceness and swiftness." --RICHARD
STRAFFORD'S LETTER FROM THE BERMUDAS. PHIL. TRANS. A.D. 1668.
''',
'''"Whales in the sea God's voice obey." --N. E. PRIMER.
''',
'''"We saw also abundance of large whales, there being more in those
southern seas, as I may say, by a hundred to one; than we have to the
northward of us." --CAPTAIN COWLEY'S VOYAGE ROUND THE GLOBE, A.D. 1729.
''',
'''"... and the breath of the whale is frequently attended with such an
insupportable smell, as to bring on a disorder of the brain." --ULLOA'S
SOUTH AMERICA.
''',
   '''  "To fifty chosen sylphs of special note,
     We trust the important charge, the petticoat.
     Oft have we known that seven-fold fence to fail,
     Tho' stuffed with hoops and armed with ribs of whale."
     --RAPE OF THE LOCK.
''',
'''"If we compare land animals in respect to magnitude, with those
that take up their abode in the deep, we shall find they will appear
contemptible in the comparison. The whale is doubtless the largest
animal in creation." --GOLDSMITH, NAT. HIST.
''',
'''"If you should write a fable for little fishes, you would make them
speak like great wales." --GOLDSMITH TO JOHNSON.'''
,
'''"In the afternoon we saw what was supposed to be a rock, but it was
found to be a dead whale, which some Asiatics had killed, and were then
towing ashore. They seemed to endeavor to conceal themselves behind the
whale, in order to avoid being seen by us." --COOK'S VOYAGES.
''',
'''"The larger whales, they seldom venture to attack. They stand in so
great dread of some of them, that when out at sea they are afraid to
mention even their names, and carry dung, lime-stone, juniper-wood,
and some other articles of the same nature in their boats, in order to
terrify and prevent their too near approach." --UNO VON TROIL'S LETTERS
ON BANKS'S AND SOLANDER'S VOYAGE TO ICELAND IN 1772.
''',
'''"The Spermacetti Whale found by the Nantuckois, is an active, fierce
animal, and requires vast address and boldness in the fishermen."
--THOMAS JEFFERSON'S WHALE MEMORIAL TO THE FRENCH MINISTER IN 1778.
''',
'''"And pray, sir, what in the world is equal to it?" --EDMUND BURKE'S
REFERENCE IN PARLIAMENT TO THE NANTUCKET WHALE-FISHERY.
''',
'''"Spain--a great whale stranded on the shores of Europe." --EDMUND BURKE.
(SOMEWHERE.)
''',
'''"A tenth branch of the king's ordinary revenue, said to be grounded on
the consideration of his guarding and protecting the seas from pirates
and robbers, is the right to royal fish, which are whale and sturgeon.
And these, when either thrown ashore or caught near the coast, are the
property of the king." --BLACKSTONE.
''',
   '''  "Soon to the sport of death the crews repair:
     Rodmond unerring o'er his head suspends
     The barbed steel, and every turn attends."
     --FALCONER'S SHIPWRECK.
''',
   '''  "Bright shone the roofs, the domes, the spires,
     And rockets blew self driven,
     To hang their momentary fire
     Around the vault of heaven.
'  "So fire with water to compare,
     The ocean serves on high,
     Up-spouted by a whale in air,
     To express unwieldy joy." --COWPER, ON THE QUEEN'S
     VISIT TO LONDON.
''',
'''"Ten or fifteen gallons of blood are thrown out of the heart at
a stroke, with immense velocity." --JOHN HUNTER'S ACCOUNT OF THE
DISSECTION OF A WHALE. (A SMALL SIZED ONE.)
''',
   '''
"The aorta of a whale is larger in the bore than the main pipe of the
water-works at London Bridge, and the water roaring in its passage
through that pipe is inferior in impetus and velocity to the blood
gushing from the whale's heart." --PALEY'S THEOLOGY.
''',

   '''
"The whale is a mammiferous animal without hind feet." --BARON CUVIER.
''',
   '''
"In 40 degrees south, we saw Spermacetti Whales, but did not take
any till the first of May, the sea being then covered with them."
--COLNETT'S VOYAGE FOR THE PURPOSE OF EXTENDING THE SPERMACETI WHALE
FISHERY.
''',
   '''  "In the free element beneath me swam,
     Floundered and dived, in play, in chace, in battle,
     Fishes of every colour, form, and kind;
     Which language cannot paint, and mariner
     Had never seen; from dread Leviathan
     To insect millions peopling every wave:
     Gather'd in shoals immense, like floating islands,
     Led by mysterious instincts through that waste
     And trackless region, though on every side
     Assaulted by voracious enemies,
     Whales, sharks, and monsters, arm'd in front or jaw,
     With swords, saws, spiral horns, or hooked fangs."
     --MONTGOMERY'S WORLD BEFORE THE FLOOD.
''',
   '''  "Io!  Paean!  Io! sing.
     To the finny people's king.
     Not a mightier whale than this
     In the vast Atlantic is;
     Not a fatter fish than he,
     Flounders round the Polar Sea."
     --CHARLES LAMB'S TRIUMPH OF THE WHALE.
''',
'''"In the year 1690 some persons were on a high hill observing the
whales spouting and sporting with each other, when one observed:
there--pointing to the sea--is a green pasture where our children's
grand-children will go for bread." --OBED MACY'S HISTORY OF NANTUCKET.
''',

'''"I built a cottage for Susan and myself and made a gateway in the form
of a Gothic Arch, by setting up a whale's jaw bones." --HAWTHORNE'S
TWICE TOLD TALES.
''',
'''"She came to bespeak a monument for her first love, who had been killed
by a whale in the Pacific ocean, no less than forty years ago." --IBID.
''',
'''"No, Sir, 'tis a Right Whale," answered Tom; "I saw his sprout; he threw
up a pair of as pretty rainbows as a Christian would wish to look at.
He's a raal oil-butt, that fellow!" --COOPER'S PILOT.
''',
'''"The papers were brought in, and we saw in the Berlin Gazette
that whales had been introduced on the stage there." --ECKERMANN'S
CONVERSATIONS WITH GOETHE.
''',
'''"My God! Mr. Chace, what is the matter?" I answered, "we have been stove
by a whale." --"NARRATIVE OF THE SHIPWRECK OF THE WHALE SHIP ESSEX OF
NANTUCKET, WHICH WAS ATTACKED AND FINALLY DESTROYED BY A LARGE SPERM
WHALE IN THE PACIFIC OCEAN." BY OWEN CHACE OF NANTUCKET, FIRST MATE OF
SAID VESSEL. NEW YORK, 1821.
''',
   '''  "A mariner sat in the shrouds one night,
     The wind was piping free;
     Now bright, now dimmed, was the moonlight pale,
     And the phospher gleamed in the wake of the whale,
     As it floundered in the sea."
     --ELIZABETH OAKES SMITH.
''',
'''"The quantity of line withdrawn from the boats engaged in the capture
of this one whale, amounted altogether to 10,440 yards or nearly six
English miles....
''',
'''"Sometimes the whale shakes its tremendous tail in the air, which,
cracking like a whip, resounds to the distance of three or four miles."
--SCORESBY.
''',
'''"Mad with the agonies he endures from these fresh attacks, the
infuriated Sperm Whale rolls over and over; he rears his enormous head,
and with wide expanded jaws snaps at everything around him; he rushes
at the boats with his head; they are propelled before him with vast
swiftness, and sometimes utterly destroyed.... It is a matter of great
astonishment that the consideration of the habits of so interesting,
and, in a commercial point of view, so important an animal (as the Sperm
Whale) should have been so entirely neglected, or should have excited
so little curiosity among the numerous, and many of them competent
observers, that of late years, must have possessed the most abundant
and the most convenient opportunities of witnessing their habitudes."
--THOMAS BEALE'S HISTORY OF THE SPERM WHALE, 1839.
''',
'''"The Cachalot" (Sperm Whale) "is not only better armed than the True
Whale" (Greenland or Right Whale) "in possessing a formidable weapon
at either extremity of its body, but also more frequently displays a
disposition to employ these weapons offensively and in manner at once so
artful, bold, and mischievous, as to lead to its being regarded as the
most dangerous to attack of all the known species of the whale tribe."
--FREDERICK DEBELL BENNETT'S WHALING VOYAGE ROUND THE GLOBE, 1840.
''',
   '''  October 13.  "There she blows," was sung out from the mast-head.
     "Where away?" demanded the captain.
     "Three points off the lee bow, sir."
     "Raise up your wheel.  Steady!"  "Steady, sir."
     "Mast-head ahoy!  Do you see that whale now?"
     "Ay ay, sir!  A shoal of Sperm Whales!  There she blows!  There she
     breaches!"
     "Sing out! sing out every time!"
     "Ay Ay, sir!  There she blows! there--there--THAR she
     blows--bowes--bo-o-os!"
     "How far off?"
     "Two miles and a half."
     "Thunder and lightning! so near!  Call all hands."
     --J. ROSS BROWNE'S ETCHINGS OF A WHALING CRUIZE.  1846.
''',
'''"The Whale-ship Globe, on board of which vessel occurred the horrid
transactions we are about to relate, belonged to the island of
Nantucket." --"NARRATIVE OF THE GLOBE," BY LAY AND HUSSEY SURVIVORS.
A.D. 1828.
''',
'''Being once pursued by a whale which he had wounded, he parried the
assault for some time with a lance; but the furious monster at length
rushed on the boat; himself and comrades only being preserved by leaping
into the water when they saw the onset was inevitable." --MISSIONARY
JOURNAL OF TYERMAN AND BENNETT.
''',
'''"Nantucket itself," said Mr. Webster, "is a very striking and peculiar
portion of the National interest. There is a population of eight or nine
thousand persons living here in the sea, adding largely every year
to the National wealth by the boldest and most persevering industry."
--REPORT OF DANIEL WEBSTER'S SPEECH IN THE U. S. SENATE, ON THE
APPLICATION FOR THE ERECTION OF A BREAKWATER AT NANTUCKET. 1828.
''',
'''"The whale fell directly over him, and probably killed him in a moment."
--"THE WHALE AND HIS CAPTORS, OR THE WHALEMAN'S ADVENTURES AND THE
WHALE'S BIOGRAPHY, GATHERED ON THE HOMEWARD CRUISE OF THE COMMODORE
PREBLE." BY REV. HENRY T. CHEEVER.
''',
'''"If you make the least damn bit of noise," replied Samuel, "I will send
you to hell." --LIFE OF SAMUEL COMSTOCK (THE MUTINEER), BY HIS BROTHER,
WILLIAM COMSTOCK. ANOTHER VERSION OF THE WHALE-SHIP GLOBE NARRATIVE.
''',
'''"The voyages of the Dutch and English to the Northern Ocean, in order,
if possible, to discover a passage through it to India, though they
failed of their main object, laid-open the haunts of the whale."
--MCCULLOCH'S COMMERCIAL DICTIONARY.
''',
'''"These things are reciprocal; the ball rebounds, only to bound forward
again; for now in laying open the haunts of the whale, the whalemen seem
to have indirectly hit upon new clews to that same mystic North-West
Passage." --FROM "SOMETHING" UNPUBLISHED.
''',
'''"It is impossible to meet a whale-ship on the ocean without being struck
by her near appearance. The vessel under short sail, with look-outs at
the mast-heads, eagerly scanning the wide expanse around them, has a
totally different air from those engaged in regular voyage." --CURRENTS
AND WHALING. U.S. EX. EX.
''',
'''"Pedestrians in the vicinity of London and elsewhere may recollect
having seen large curved bones set upright in the earth, either to form
arches over gateways, or entrances to alcoves, and they may perhaps
have been told that these were the ribs of whales." --TALES OF A WHALE
VOYAGER TO THE ARCTIC OCEAN.
''',
'''"It was not till the boats returned from the pursuit of these whales,
that the whites saw their ship in bloody possession of the savages
enrolled among the crew." --NEWSPAPER ACCOUNT OF THE TAKING AND RETAKING
OF THE WHALE-SHIP HOBOMACK.
''',
'''"It is generally well known that out of the crews of Whaling vessels
(American) few ever return in the ships on board of which they
departed." --CRUISE IN A WHALE BOAT.
''',
'''"Suddenly a mighty mass emerged from the water, and shot up
perpendicularly into the air. It was the whale." --MIRIAM COFFIN OR THE
WHALE FISHERMAN.
''',
'''"The Whale is harpooned to be sure; but bethink you, how you would
manage a powerful unbroken colt, with the mere appliance of a rope tied
to the root of his tail." --A CHAPTER ON WHALING IN RIBS AND TRUCKS.
''',

'''"On one occasion I saw two of these monsters (whales) probably male and
female, slowly swimming, one after the other, within less than a stone's
throw of the shore" (Terra Del Fuego), "over which the beech tree
extended its branches." --DARWIN'S VOYAGE OF A NATURALIST.
''',

'''"'Stern all!' exclaimed the mate, as upon turning his head, he saw the
distended jaws of a large Sperm Whale close to the head of the boat,
threatening it with instant destruction;--'Stern all, for your lives!'"
--WHARTON THE WHALE KILLER.
''',
'''"So be cheery, my lads, let your hearts never fail, While the bold
harpooneer is striking the whale!" --NANTUCKET SONG.
''',
   '''  "Oh, the rare old Whale, mid storm and gale
     In his ocean home will be
     A giant in might, where might is right,
     And King of the boundless sea."
     --WHALE SONG
    ''']

if __name__ == "__main__":
    print(quote())
