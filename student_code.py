from collections import Counter

# Fonction pour découper le texte en paires de caractères
def cut_string_into_pairs(text):
    pairs = []
    for i in range(0, len(text) - 1, 2):
        pairs.append(text[i:i + 2])
    if len(text) % 2 != 0:
        pairs.append(text[-1] + '_')  # Ajouter un caractère de remplissage si le texte est impair
    return pairs

# Fonction pour compter le nombre de mots dans un texte
def count_words(text):
    words = text.split()
    return len(words)

# Texte de 1000 mots que tu ajouteras ici
texte_1000_mots = """"
Lorsque les cendres de DESCARTES, né en France et mort en Suède, furent
rapportées, seize ans après sa mort, de Stockholm à Paris; lorsque tous
les savants, rassemblés dans un temple, rendoient à sa dépouille des
honneurs qu'il n'obtint jamais pendant sa vie, et qu'un orateur se
préparait à louer devant cette assemblée le grand homme qu'elle
regrettait, tout-à-coup il vint un ordre qui défendit de prononcer cet
éloge funèbre. Sans doute on pensoit alors que les grands seuls ont
droit aux éloges publics; et l'on craignit de donner à la nation
l'exemple dangereux d'honorer un homme qui n'avoit eu que le mérite et
la distinction du génie. Je viens, après cent ans, prononcer cet éloge.
Puisse-t-il être digne et de celui à qui il est offert, et des sages qui
vont l'entendre! Peut-être au siècle de Descartes on étoit encore trop
près de lui pour le bien louer. Le temps seul juge les philosophes comme
les rois, et les met à leur place.

Le temps a détruit les opinions de Descartes, mais sa gloire subsiste.
Il est semblable à ces rois détrônés qui, sur les ruines même de
leur empire, paroissent nés pour commander aux hommes. Tant que la
philosophie et la vérité seront quelque chose sur la terre, on honorera
celui qui a jeté les fondements de nos connaissances, et recréé, pour
ainsi dire, l'entendement humain. On louera Descartes par admiration,
par reconnoissance, par intérêt même; car si la vérité est un bien, il
faut encourager ceux qui la cherchent.

Ce seroit aux pieds de la statue de Newton qu'il faudroit prononcer
l'éloge de Descartes; ou plutôt ce seroit à Newton à louer Descartes.
Qui mieux que lui seroit capable de mesurer la carrière parcourue avant
lui? Aussi simple qu'il étoit grand, Newton nous découvriroit toutes les
pensées que les pensées de Descartes lui ont fait naître. Il y a des
vérités stériles, et pour ainsi dire mortes, qui n'avancent de rien dans
l'étude de la nature: il y a des erreurs de grands hommes qui deviennent
fécondes en vérités. Après Descartes, on a été plus loin que lui; mais
Descartes a frayé la route. Louons Magellan d'avoir fait le tour du
globe; mais rendons justice à Colomb, qui le premier a soupçonné, a
cherché, a trouvé un nouveau monde.

Tout dans cet ouvrage sera consacré à la philosophie et à la vertu.
Peut-être y a-t-il des hommes dans ma nation qui ne me pardonneroient
point l'éloge d'un philosophe vivant; mais Descartes est mort, et depuis
cent quinze ans il n'est plus; je ne crains ni de blesser l'orgueil ni
d'irriter l'envie.

Pour juger Descartes, pour voir ce que l'esprit d'un seul homme a ajouté
à l'esprit humain, il faut voir le point d'où il est parti. Je peindrai
donc l'état de la philosophie et des sciences au moment où naquit ce
grand homme; je ferai voir comment la nature le forma, et comment elle
prépara cette révolution qui a eu tant d'influence. Ensuite je ferai
l'histoire de ses pensées. Ses erreurs mêmes auront je ne sais quoi
de grand. Ou verra l'esprit humain, frappé d'une lumière nouvelle, se
réveiller, s'agiter, et marcher sur ses pas. Le mouvement philosophique
se communiquera d'un bout de l'Europe à l'autre. Cependant, au milieu de
ce mouvement général, nous reviendrons sur Descartes; nous contemplerons
l'homme en lui; nous chercherons si le génie donne des droits au
bonheur; et nous finirons peut-être par répandre des larmes sur ceux
qui, pour le bien de l'humanité et leur propre malheur, sont condamnés à
être de grands hommes.

La philosophie, née dans l'Égypte, dans l'Inde et dans la Perse, avoit
été en naissant presque aussi barbare que les hommes. Dans la Grèce,
aussi féconde que hardie, elle avoit créé tous ces systèmes qui
expliquoient l'univers, ou par le principe des éléments, ou par
l'harmonie des nombres, ou par les idées éternelles, ou par des
combinaisons de masses, de figures et de mouvements, ou par l'activité
de la forme qui vient s'unir à la matière. Dans Alexandrie, et à la
cour des rois, elle avoit perdu ce caractère original et ce principe de
fécondité que lui avoit donné un pays libre. A Rome, parmi des maîtres
et des esclaves, elle avoit été également stérile; elle s'y étoit
occupée, ou à flatter la curiosité des princes, ou à lire dans les
astres la chute des tyrans. Dans les premiers siècles de l'église, vouée
aux enchantements et aux mystères, elle avoit cherché à lier commerce
avec les puissances célestes ou infernales. Dans Constantinople, elle
avoit tourné autour des idées des anciens Grecs, comme autour des bornes
du monde. Chez les Arabes, chez ce peuple doublement esclave et par
sa religion et par son gouvernement, elle avoit eu ce même caractère
d'esclavage, bornée à commenter un homme, au lieu d'étudier la nature.
Dans les siècles barbares de l'Occident, elle n'avoit été qu'un jargon
absurde et insensé que consacroit le fanatisme et qu'adoroit la
superstition. Enfin, à la renaissance des lettres, elle n'avoit profité
de quelques lumières que pour se remettre par choix dans les chaînes
d'Aristote. Ce philosophe, depuis plus de cinq siècles, combattu,
proscrit, adoré, excommunié, et toujours vainqueur, dictoit aux nations
ce qu'elles devoient croire; ses ouvrages étant plus connus, ses erreurs
étoient plus respectées. On négligeoit pour lui l'univers; et les
hommes, accoutumés depuis longtemps à se passer de l'évidence, croyoient
tenir dans leurs mains les premiers principes des choses, parce que leur
ignorance hardie prononçoit des mots obscurs et vagues qu'ils croyoient
entendre.

Voilà les progrès que l'esprit humain avoit faits pendant trente
siècles. On remarque, pendant cette longue révolution de temps, cinq
ou six hommes qui ont pensé, et créé des idées; et le reste du monde a
travaillé sur ces pensées, comme l'artisan, dans sa forge, travaille sur
les métaux que lui fournit la mine. Il y a eu plusieurs siècles de suite
où l'on n'a point avancé d'un pas vers la vérité; il y a eu des nations
qui n'ont pas contribué d'une idée à la masse des idées générales. Du
siècle d'Aristote à celui de Descartes, j'aperçois un vide de deux mille
ans. Là, la pensée originale se perd, comme un fleuve qui meurt dans les
sables, ou qui s'ensevelit sous terre, et qui ne reparoît qu'à mille
lieues de là, sous de nouveaux cieux et sur une terre nouvelle. Quoi
donc! y a-t-il pour l'esprit humain des temps de sommeil et de mort,
comme il y en a de vie et d'activité? ou le don de penser par
soi-même est-il réservé à un si petit nombre d'hommes? ou les
grandes combinaisons d'idées sont-elles bornées par la nature, et
s'épuisent-elles avec rapidité? Dans cet état de l'esprit humain, dans
cet engourdissement général, il falloit un homme qui remontât l'espèce
humaine, qui ajoutât de nouveaux ressorts à l'entendement, qui se
ressaisît du don de penser, qui vît ce qui étoit fait, ce qui restoit à
faire, et pourquoi les progrès avoient été suspendus tant de siècles;
un homme qui eût assez d'audace pour renverser, assez de génie pour
reconstruire, assez de sagesse pour poser des fondements sûrs, assez
d'éclat pour éblouir son siècle et rompre l'enchantement des siècles
passés; un homme qui étonnât par la grandeur de ses vues; un homme en
état de rassembler tout ce que les sciences avoient imaginé ou découvert
dans tous les siècles, et de réunir toutes ces forces dispersées pour
en composer une seule force avec laquelle il remuât pour ainsi dire
l'univers; un homme d'un génie actif, entreprenant, qui sût voir où
personne ne voyoit, qui désignât le but et qui traçât la route, qui,
seul et sans guide, franchît par-dessus les précipices un intervalle
immense, et entraînât après lui le genre humain. Cet homme devoit être
Descartes. Ce seroit sans doute un beau spectacle de voir comment la
nature le prépara du loin et le forma; mais qui peut suivre la nature
dans sa marche? Il y a sans doute une chaîne des pensées des hommes
depuis l'origine du monde jusqu'à nous; chaîne qui n'est ni moins
mystérieuse ni moins grande que celle des êtres physiques. Les siècles
ont influé sur les siècles, les nations sur les nations, les vérités sur
les erreurs, les erreurs sur les vérités. Tout se tient dans l'univers;
mais qui pourrait tracer la ligne? On peut du moins entrevoir ce rapport
général; on peut dire que, sans cette foule d'erreurs qui ont inondé le
monde, Descartes peut-être n'eût point trouvé la route de la vérité.
Ainsi chaque philosophe en s'égarant avançoit le terme. Mais, laissant
là les temps trop reculés, je veux chercher dans le siècle même de
Descartes, ou dans ceux qui ont immédiatement précédé sa naissance, tout
ce qui a pu servir à le former en influant sur son génie.

Et d'abord j'aperçois dans l'univers une espèce de fermentation
générale. La nature semble être dans un de ces moments où elle fait les
plus grands efforts: tout s'agite; on veut partout remuer les anciennes
bornes, on veut étendre la sphère humaine. Vasco de Gama découvre les
Indes, Colomb découvre l'Amérique, Cortès et Pizarro subjuguent des
contrées immenses et nouvelles, Magellan cherche les terres australes,
Drake fait le tour du monde. L'esprit des découvertes anime toutes
les nations. De grands changements dans la politique et les religions
ébranlent l'Europe, l'Asie et l'Afrique. Cette secousse se communique
aux sciences. L'astronomie renaît dès le quinzième siècle. Copernic
rétablit le système de Pythagore et le mouvement de la terre; pas
immense fait dans la nature! Tycho-Brahé ajoute aux observations de
tous les siècles; il corrige et perfectionne la théorie des planètes,
détermine le lieu d'un grand nombre d'étoiles fixes, démontre la région
que les comètes occupent dans l'espace. Le nombre des phénomènes connus
s'augmente. Le législateur des deux paroît; Kepler confirme ce qui a été
trouvé avant lui, et ouvre la route à des vérités nouvelles. Mais
il falloit de plus grands secours. Les verres concaves et convexes,
inventés par hasard au treizième siècle, sont réunis trois cents ans
après, et forment le premier télescope. L'homme touche aux extrémités de
la création. Galilée fait dans les cieux ce que les grands navigateurs
faisoient sur les mers; il aborde à de nouveaux mondes. Les satellites
de Jupiter sont connus. Le mouvement de la terre est confirmé par les
phases de Vénus. La géométrie est appliquée à la doctrine du mouvement.
La force accélératrice dans la chute des corps est mesurée; on découvre
la pesanteur de l'air, on entrevoit son élasticité. Bacon fait le
dénombrement des connoissances humaines et les juge: il annonce le
besoin de refaire des idées nouvelles, et prédit quelque chose de
grand pour les siècles à venir. Voilà ce que la nature avoit fait pour
Descartes avant sa naissance; et comme par la boussole elle avoit réuni
les parties les plus éloignées du globe, par le télescope rapproché de
la terre les dernières limites des cieux, par l'imprimerie elle avoit
établi la communication rapide du mouvement entre les esprits d'un bout
du monde à l'autre.

Tout étoit disposé pour une révolution. Déjà est né celui qui doit
faire ce grand changement[1]; il ne reste à la nature que d'achever son
ouvrage, et de mûrir Descartes pour le genre humain, comme elle a mûri
le genre humain pour lui. Je ne m'arrête point sur son éducation[2]; dès
qu'il s'agit des âmes extraordinaires, il n'en faut point parler. Il y
a une éducation pour l'homme vulgaire; il n'y en a point d'autre pour
l'homme de génie que celle qu'il se donne à lui-même: elle consiste
presque toujours à détruire la première. Descartes, par celle qu'il
reçut, jugea son siècle. Déjà il voit au-delà; déjà il imagine et
pressent un nouvel ordre des sciences: tel, de Madrid ou de Gènes,
Colomb pressentoit l'Amérique.

La nature, qui travailloit sur cette âme et la disposoit insensiblement
aux grandes choses, y avoit mis d'abord une forte passion pour la
vérité. Ce fut là peut-être son premier ressort. Elle y ajoute ce désir
d'être utile aux hommes, qui s'étend à tous les siècles et à toutes les
nations; désir qu'on ne s'étoit point encore avisé de calomnier. Elle
lui donne ensuite, pour tout le temps de sa jeunesse, une activité
inquiète[3], ces tourments du génie, ce vide d'une âme que rien ne
remplit encore, et qui se fatigue à chercher autour d'elle ce qui doit
la fixer. Alors elle le promène dans l'Europe entière, et fait passer
rapidement sous ses yeux les plus grands spectacles. Elle lui présente,
en Hollande, un peuple qui brise ses chaînes et devient libre, le
fanatisme germant au sein de la liberté, les querelles de la religion
changées en factions d'état; en Allemagne, le choc de la ligue
protestante et de la ligue catholique, le commencement d'un carnage de
trente années; aux extrémités de la Pologne, dans le Brandebourg, la
Poméranie et le Holstein, les contre-coups de cette guerre affreuse;
en Flandre, le contraste de dix provinces opulentes restées soumises
à l'Espagne, tandis que sept provinces pauvres combattoient depuis
cinquante ans pour leur liberté; dans la Valteline, les mouvements de
l'ambition espagnole, les précautions inquiètes de la cour de Savoie;
eu Suisse, des lois et des moeurs, une pauvreté fière, une liberté sans
orages; à Gênes, toutes les factions des républiques, tout l'orgueil des
monarchies; à Venise, le pouvoir des nobles, l'esclavage du peuple, une
liberté tyrannique; à Florence, les Médicis, les arts, et Galilée; à
Rome, toutes les nations rassemblées par la religion, spectacle qui vaut
peut-être bien celui des statues et des tableaux; en Angleterre, les
droits des peuples luttant contre ceux des rois, Charles Ier sur le
trône, et Cromwell encore dans la foule[4]. L'âme de Descartes, à
travers tous ces objets, s'élève et s'agrandit. La religion, la
politique, la liberté, la nature, la morale, tout contribue à étendre
ses idées; car l'on se trompe si l'on croit que l'âme du philosophe
doit se concentrer dans l'objet particulier qui l'occupe. Il doit tout
embrasser, tout voir. Il y a des points de réunion où toutes les vérités
se touchent; et la vérité universelle n'est elle-même que la chaîne de
tous les rapports. Pour voir de plus près le genre humain sous toutes
les faces, Descartes se mêle dans ces jeux sanglants des rois, où le
génie s'épuise à détruire, et où des milliers d'hommes, assemblés contre
des milliers d'hommes, exercent le meurtre par art et par principes[5].
Ainsi Socrate porta les armes dans sa jeunesse. Partout il étudie
l'homme et le monde. Il analyse l'esprit humain; il observe les
opinions, suit leur progrès, examine leur influence, remonte à leur
source. De ces opinions, les unes naissent du gouvernement, d'autres
du climat, d'autres de la religion, d'autres de la forme des langues,
quelques unes des moeurs, d'autres des lois, plusieurs de toutes ces
causes réunies: il y en a qui sortent du fond même de l'esprit humain et
de la constitution de l'homme, et celles-là sont à peu près les mêmes
chez tous les peuples; il y en a d'autres qui sont bornées par les
montagnes et par les fleuves, car chaque pays a ses opinions comme ses
plantes: toutes ensemble forment la raison du peuple. Quel spectacle
pour un philosophe! Descartes en fut épouvanté. Voilà donc, dit-il, la
raison humaine! Dès ce moment il sentit s'ébranler tout l'édifice de ses
connoissances: il voulut y porter la main pour achever de le renverser;
mais il n'avoit point encore assez de force, et il s'arrêta. Il poursuit
ses observations; il étudie la nature physique: tantôt il la considère
dans toute son étendue, comme ne formant qu'un seul et immense ouvrage;
tantôt il la suit dans ses détails. La nature vivante et la nature
morte, l'être brut et l'être organisé, les différentes classes de
grandeurs et de formes, les destructions et les renouvellements, les
variétés et les rapports, rien ne lui échappe, comme rien ne l'étonne.
J'aime à le voir debout sur la cime des Alpes, élevé, par sa situation,
au-dessus de l'Europe entière, suivant de l'oeil la course du Pô, du
Rhin, du Rhône et du Danube, et de là s'élevant par la pensée vers les
deux, qu'il paroît toucher, pénétrant dans les réservoirs destinés à
fournir à l'Europe ces amas d'eaux immenses; quelquefois observant à ses
pieds les espèces innombrables de végétaux semés par la nature sur le
penchant des précipices, ou entre les pointes des rochers; quelquefois
mesurant la hauteur de ces montagnes de glace, qui semblent jetées dans
les vallons des Alpes pour les combler, ou méditant profondément à la
lueur des orages[6]. Ah! c'est dans ces moments que l'âme du philosophe
s'étend, devient immense et profonde comme la nature; c'est alors que
ses idées s'élèvent et parcourent l'univers. Insatiable de voir et de
connoître, partout où il passe, Descartes interroge la vérité; il la
demande à tous les lieux qu'il parcourt, il la poursuit de pays en pays.
Dans les villes prises d'assaut, ce sont les savants qu'il cherche.
Maximilien de Bavière voit dans Prague, dont il s'est rendu maître, la
capitale d'un royaume conquis; Descartes n'y voit que l'ancien séjour de
Tycho-Brahé. Sa mémoire y étoit encore récente; il interroge tous ceux
qui l'ont connu, il suit les traces de ses pensées; il rassemble dans
les conversations le génie d'un grand homme. Ainsi voyageoient autrefois
les Pythagore, et les Platon, lorsqu'ils alloient dans l'Orient étudier
ces colonnes, archives des nations et monuments des découvertes
antiques. Descartes, à leur exemple, ramasse tout ce qui peut
l'instruire. Mais tant d'idées acquises dans ses voyages ne lui auroient
encore servi de rien, s'il n'avoit eu l'art de se les approprier par des
méditations profondes; art si nécessaire au philosophe, si inconnu au
vulgaire, et peut-être si étranger à l'homme. En effet, qu'est-ce que
méditer? C'est ramener au dedans de nous notre existence répandue tout
entière au dehors; c'est nous retirer de l'univers pour habiter dans
notre âme; c'est anéantir toute l'activité des sens pour augmenter
celle de la pensée; c'est rassembler en un point toutes les forces de
l'esprit; c'est mesurer le temps, non plus par le mouvement et par
l'espace, mais par la succession lente ou rapide des idées. Ces
méditations, dans Descartes, avoient tourné en habitude[7]; elles
le suivoient partout: dans les voyages, dans les camps, dans les
occupations les plus tumultueuses, il avoit toujours un asile prêt où
son âme se retiroit au besoin. C'étoit là qu'il appeloit ses idées;
elles accouroient en foule: la méditation les faisoit naître, l'esprit
géométrique venoit les enchaîner. Dès sa jeunesse il s'étoit avidement
attaché aux mathématiques, comme au seul objet qui lui présentoit
l'évidence[8]. C'étoit là que son âme se reposoit de l'inquiétude qui
la tourmentoit partout ailleurs. Mais, dégoûté bientôt de spéculations
abstraites, le désir de se rapprocher des hommes le rentraînoit à
l'étude de la nature. Il se livroit à toutes les sciences: il n'y
trouvoit pas la certitude de la géométrie, qu'elle ne doit qu'à la
simplicité de son objet; mais il y transportoit du moins la méthode des
géomètres. C'est d'elle qu'il apprenoit à fixer toujours le sens des
termes, et à n'en abuser jamais; à décomposer l'objet de son étude,
à lier les conséquences aux principes; à remonter par l'analyse, à
descendre par la synthèse. Ainsi l'esprit géométrique affermissoit sa
marche; mais le courage et l'esprit d'indépendance brisoient devant lui
les barrières pour lui frayer des routes. Il étoit né avec l'audace qui
caractérise le génie; et sans doute les événements dont il avoit été
témoin, les grands spectacles de liberté qu'il avoit vus en Allemagne,
en Hollande, dans la Hongrie et dans la Bohème, avoient contribué à
développer encore en lui cette fierté d'esprit naturelle. Il osa donc
concevoir l'idée de s'élever contre les tyrans de la raison. Mais, avant
de détruire tous les préjugés qui étoient sur la terre, il falloit
commencer par les détruire en lui-même. Comment y parvenir? comment
anéantir des formes qui ne sont point notre ouvrage, et qui sont le
résultat nécessaire de mille combinaisons faites sans nous? Il falloit,
pour ainsi dire, détruire son âme et la refaire. Tant de difficultés
n'effrayèrent point Descartes. Je le vois, pendant près de dix ans,
luttant contre lui-même pour secouer toutes ses opinions. Il demande
compte à ses sens de toutes les idées qu'ils ont portées dans son âme;
il examine tous les tableaux de son imagination, et les compare avec
les objets réels; il descend dans l'intérieur de ses perceptions, qu'il
analyse; il parcourt le dépôt de sa mémoire, et juge tout ce qui y est
rassemblé. Partout il poursuit le préjugé, il le chasse de retraite en
retraite; son entendement, peuplé auparavant d'opinions et d'idées,
devient un désert immense, mais où désormais la vérité peut entrer[9].

Voilà donc la révolution faite dans l'âme de Descartes: voilà ses idées
anciennes détruites. Il ne s'agit plus que d'en créer d'autres. Car,
pour changer les nations, il ne suffit point d'abattre; il faut
reconstruire. Dès ce moment, Descartes ne pense plus qu'à élever une
philosophie nouvelle. Tout l'y invite; les exhortations de ses amis, le
désir de combler le vide qu'il avoit fait dans ses idées, je ne sais
quel instinct qui domine le grand homme, et, plus que tout cela,
l'ambition de faire des découvertes dans la nature, pour rendre les
hommes moins misérables ou plus heureux. Mais, pour exécuter un pareil
dessein, il sentit qu'il falloit se cacher. Hommes du monde, si fiers
de votre politesse et de vos avantages, souffrez que je vous dise la
vérité; ce n'est jamais parmi vous que l'on fera ni que l'on pensera
de grandes choses. Vous polissez l'esprit, mais vous énervez le génie.
Qu'a-t-il besoin de vos vains ornements? Sa grandeur fait sa beauté.
C'est dans la solitude que l'homme de génie est ce qu'il doit être;
c'est là qu'il rassemble toutes les forces de son âme. Auroit-il besoin
des hommes? N'a-t-il pas avec lui la nature? et il ne la voit point
à travers les petites formes de la société, mais dans sa grandeur
primitive, dans sa beauté originale et pure. C'est dans la solitude
que toutes les heures laissent une trace, que tous les instants sont
représentés par une pensée, que le temps est au sage, et le sage à
lui-même. C'est dans la solitude surtout que l'âme a toute la vigueur
de l'indépendance. Là elle n'entend point le bruit des chaînes que le
despotisme et la superstition secouent sur leurs esclaves: elle
est libre comme la pensée de l'homme qui existeroit seul. Cette
indépendance, après la vérité, étoit la plus grande passion de
Descartes. Ne vous en étonnez point; ces deux passions tiennent l'une à
l'autre. La vérité est l'aliment d'une âme fière et libre, tandis que
l'esclave n'ose même lever les yeux jusqu'à elle. C'est cet amour de la
liberté qui engage Descartes à fuir tous les engagements, à rompre tous
les petits liens de société, à renoncer à ces emplois qui ne sont trop
souvent que les chaînes de l'orgueil. Il falloit qu'un homme comme lui
ne fût qu'à la nature et au genre humain. Descartes ne fut donc ni
magistrat, ni militaire, ni homme de cour[10]. Il consentit à n'être
qu'un philosophe, qu'un homme de génie, c'est-à-dire rien aux yeux du
peuple. Il renonce même à son pays; il choisit une retraite dans la
Hollande. C'est dans le séjour de la liberté qu'il va fonder une
philosophie libre. Il dit adieu à ses parents, à ses amis, à sa patrie;
il part[11]. L'amour de la vérité n'est plus dans son coeur un sentiment
ordinaire; c'est un sentiment religieux qui élève et remplit son âme.
Dieu, la nature, les hommes, voilà quels vont être, le reste de sa vie,
les objets de ses pensées. Il se consacre à cette occupation aux pieds
des autels. O jour, ô moment remarquable dans l'histoire de l'esprit
humain! Je crois voir Descartes, avec le respect dont il étoit pénétré
pour la Divinité, entrer dans le temple, et s'y prosterner. Je crois
l'entendre dire à Dieu: O Dieu, puisque tu m'as créé, je ne veux point
mourir sans avoir médité sur tes ouvrages. Je vais chercher la vérité,
si tu l'as mise sur la terre. Je vais me rendre utile à l'homme, puisque
je suis homme. Soutiens ma foiblesse, agrandis mon esprit, rends-le
digne de la nature et de toi. Si tu permets que j'ajoute à la perfection
des hommes, je te rendrai grâce en mourant, et ne me repentirai point
d'être né.

Je m'arrête un moment: l'ouvrage de la nature est achevé. Elle a préparé
avant la naissance de Descartes tout ce qui devoit influer sur lui; elle
lui a donné les prédécesseurs dont il avoit besoin; elle a jeté dans son
sein les semences qui devoient y germer; elle a établi entre son esprit
et son âme les rapports nécessaires; elle a fait passer sous ses yeux
tous les grands spectacles et du monde physique et du monde moral; elle
a rassemblé autour de lui, ou dans lui, tous les ressorts; elle a mis
dans sa main tous les instruments: son travail est fini. Ici commence
celui de Descartes. Je vais faire l'histoire de ses pensées: on verra
une espèce de création; elle embrassera tout ce qui est; elle présentera
une machine immense, mue avec peu de ressorts: on y trouvera le grand
caractère de la simplicité, l'enchaînement de toutes les parties, et
souvent, comme dans la nature physique, un ordre réel caché sous un
désordre apparent.

Je commence par où il a commencé lui-même. Avant de mettre la main à
l'édifice, il faut jeter les fondements; il faut creuser jusqu'à la
source de la vérité; il faut établir l'évidence, et distinguer son
caractère. Nous avons vu Descartes renverser toutes les fausses
opinions qui étoient dans son âme; il fait plus, il s'élève à un doute
universel[12]. Celui qui s'est trompé une fois peut se tromper toujours.
Aussitôt les cieux, la terre, les figures, les sons, les couleurs, son
corps même, et les sens avec lesquels il voyage dans l'univers, tout
s'anéantit à ses yeux. Rien n'est assuré, rien n'existe. Dans ce doute
général, où trouver un point d'appui? Quelle première vérité servira de
base à toutes les vérités? Pour Dieu, cette première vérité est partout.
Descartes la trouve dans son doute même. Puisque je doute, je pense;
puisque je pense, j'existe. Mais à quelle marque la reconnoît-il? A
l'empreinte de l'évidence. Il établit donc pour principe de ne regarder
comme vrai que ce qui est évident, c'est-à-dire ce qui est clairement
contenu dans l'idée de l'objet qu'il contemple. Tel est ce fameux doute
philosophique de Descartes. Tel est le premier pas qu'il fait pour en
sortir, et la première règle qu'il établit. C'est cette règle qui a fait
la révolution de l'esprit humain. Pour diriger l'entendement, il joint
l'analyse au doute. Décomposer les questions et les diviser en plusieurs
branches; avancer par degrés des objets les plus simples aux plus
composés, et des plus connus aux plus cachés; combler l'intervalle
qui est entre les idées éloignées et le remplir par toutes les idées
intermédiaires; mettre dans ces idées un tel enchaînement que toutes se
déduisent aisément les unes des autres, et que les énoncer, ce soit pour
ainsi dire les démontrer; voilà les autres règles qu'il a établies, et
dont il a donné l'exemple[13]. On entrevoit déjà toute la marche de sa
philosophie. Puisqu'il faut commencer par ce qui est évident et simple,
il établira des principes qui réunissent ce double caractère. Pour
raisonner sur la nature, il s'appuiera sur des axiomes, et déduira des
causes générales tous les effets particuliers. Ne craignons pas de
l'avouer, Descartes a tracé un plan trop élevé pour l'homme; ce génie
hardi a eu l'ambition de connoître comme Dieu même connoît, c'est-à-dire
par les principes: mais sa méthode n'en est pas moins la créatrice de
la philosophie. Avant lui, il n'y avoit qu'une logique de mots. Celle
d'Aristote apprenoit plus à définir et à diviser qu'à connoître; à tirer
les conséquences, qu'à découvrir les principes. Celle des scolastiques,
absurdement subtile, laissoit les réalités pour s'égarer dans des
abstractions barbares. Celle de Raimond Lulle n'étoit qu'un assemblage
de caractères magiques pour interroger sans entendre, et répondre sans
être entendu. C'est Descartes qui créa cette logique intérieure de
l'âme, par laquelle l'entendement se rend compte à lui-même de toutes
ses idées, calcule sa marche, ne perd jamais de vue le point d'où il
part et le terme où il veut arriver; esprit de raison plutôt que de
raisonnement, et qui s'applique à tous les arts comme à toutes les
sciences.

Sa méthode est créée: il a fait comme ces grands architectes qui,
concevant des ouvrages nouveaux, commencent par se faire de nouveaux
instruments et des machines nouvelles. Aidé de ce secours, il entre
dans la métaphysique. Il y jette d'abord un regard. Qu'aperçoit-il? une
audace puérile de l'esprit humain, des êtres imaginaires, des rêveries
profondes, des mots barbares; car, dans tous les temps, l'homme, quand
il n'a pu connoître, a créé des signes pour représenter des idées qu'il
n'avoit pas, et il a pris ces signes pour des connoissances. Descartes
vit d'un coup d'oeil ce que devoit être la métaphysique. Dieu, l'âme, et
les principes généraux des sciences, voilà ses objets[14]. Je m'élève
avec lui jusqu'à la première cause. Newton la chercha dans les mondes;
Descartes la cherche dans lui-même. Il s'étoit convaincu de l'existence
de son âme; il avoit senti en lui l'être qui pense, c'est-à-dire l'être
qui doute, qui nie, qui affirme, qui conçoit, qui veut, qui a des
erreurs, qui les combat. Cet être intelligent est donc sujet à des
imperfections. Mais toute idée d'imperfection suppose l'idée d'un être
plus parfait. De l'idée du parfait naît l'idée de l'infini. D'où lui
naît cette idée? Comment l'homme, dont les facultés sont si bornées,
l'homme qui passe sa vie à tourner dans l'intérieur d'un cercle étroit,
comment cet être si foible a-t-il pu embrasser et concevoir l'infini?
Cette idée ne lui est-elle pas étrangère? ne suppose-t-elle pas hors de
lui un être qui en soit le modèle et le principe? Cet être n'est-il pas
Dieu? Toutes les autres idées claires et distinctes que l'homme trouve
en lui ne renferment que l'existence possible de leur objet: l'idée
seule de l'être parfait renferme une existence nécessaire. Cette idée
est pour Descartes le commencement de la grande chaîne. Si tous les
êtres créés sont une émanation du premier être, si toutes les lois qui
font l'ordre physique et l'ordre moral sont, ou des rapports nécessaires
que Dieu a vus, ou des rapports qu'il a établis librement, en
connoissant ce qui est le plus conforme à ses attributs, on connoîtra
les lois primitives de la nature. Ainsi la connoissance de tous les
êtres se trouve enchaînée à celle du premier. C'est elle aussi qui
affermit la marche de l'esprit humain, et sert de base à l'évidence;
c'est elle qui, en m'apprenant que la vérité éternelle ne peut me
tromper, m'ordonne de regarder comme vrai tout ce que ma raison me
présentera comme évident.

Appuyé de ce principe, et sûr de sa marche, Descartes passe à l'analyse
de son âme. Il a remarqué que, dans son doute, l'étendue, la figure et
le mouvement s'anéantissoient pour lui. Sa pensée seule demeuroit;
seule elle restoit immuablement attachée à son être, sans qu'il lui fût
possible de l'en séparer. Il peut donc concevoir distinctement que sa
pensée existe, sans que rien n'existe autour de lui. L'âme se conçoit
donc sans le corps. De là naît la distinction de l'être pensant et de
l'être matériel. Pour juger de la nature des deux substances, Descartes
cherche une propriété générale dont toutes les autres dépendent: c'est
l'étendue dans la matière; dans l'âme, c'est la pensée. De l'étendue
naissent la figure et le mouvement; de la pensée naît la faculté de
sentir, de vouloir, d'imaginer. L'étendue est divisible de sa nature;
la pensée, simple et indivisible. Comment ce qui est simple
appartiendroit-il à un être composé de parties? comment des milliers
d'éléments, qui forment un corps, pourroient-ils former une perception
ou un jugement unique? Cependant il existe une chaîne secrète entre
l'âme et le corps. L'âme n'est-elle que semblable au pilote qui dirige
le vaisseau? Non; elle fait un tout avec le vaisseau qu'elle gouverne.
C'est donc de l'étroite correspondance qui est entre les mouvements de
l'un et les sensations ou pensées de l'autre, que dépend la liaison de
ces deux principes si divisés et si unis[15]. C'est ainsi que Descartes
tourne autour de son être, et examine tout ce qui le compose. Nourri
d'idées intellectuelles, et détaché de ses sens, c'est son âme qui le
frappe le plus. Voici une pensée faite pour étonner le peuple, mais que
le philosophe concevra sans peine. Descartes est plus sûr de l'existence
de son âme que de celle de son corps. En effet, que sont toutes les
sensations, sinon un avertissement éternel pour l'âme qu'elle existe?
Peut-elle sortir hors d'elle-même sans y rentrer à chaque instant par la
pensée? Quand je parcoure tous les objets de l'univers, ce n'est jamais
que ma pensée que j'aperçois. Mais comment cette âme franchit-elle
l'intervalle immense qui est entre elle et la matière? Ici Descartes
reprend son analyse et le fil de sa méthode. Pour juger s'il existe des
corps, il consulte d'abord ses idées. Il trouve dans son âme les idées
générales d'étendue, de grandeur, de figure, de situation, de mouvement,
et une foule de perceptions particulières. Ces idées lui apprennent bien
l'existence de la matière, comme objet mathématique, mais ne lui disent
rien de son existence physique et réelle. Il interroge ensuite son
imagination. Elle lui offre une suite de tableaux où des corps sont
représentés; sans doute l'original de ces tableaux existe, mais ce n'est
encore qu'une probabilité. Il remonte jusqu'à ses sens. Ce sont eux qui
font la communication de l'âme et de l'univers; ou plutôt ce sont eux
qui créent l'univers pour l'âme. Ils lui portent chaque portion du monde
en détail; par une métamorphose rapide, la sensation devient idée, et
l'âme voit dans cette idée, comme dans un miroir, le monde qui est hors
d'elle. Les sens sont donc les messagers de l'âme. Mais quelle foi
peut-elle ajouter à leur rapport? Souvent ce rapport la trompe.
Descartes remonte alors jusqu'à Dieu. D'un côté, la véracité de l'Être
suprême; de l'autre, le penchant irrésistible de l'homme à rapporter ses
sensations à des objets réels qui existent hors de lui: voilà les motifs
qui le déterminent, et il se ressaisit de l'univers physique qui lui
échappoit.

Ferai-je voir ce grand homme, malgré la circonspection de sa marche,
s'égarant dans la métaphysique, et créant son système des idées innées?
Mais cette erreur même tenoit à son génie. Accoutumé à des méditations
profondes, habitué à vivre loin des sens, à chercher dans son âme
ou dans l'essence de Dieu, l'origine, l'ordre et le fil de ses
connoissances, pouvoit-il soupçonner que l'âme fût entièrement
dépendante des sens pour les idées? N'étoit-il pas trop avilissant
pour elle qu'elle ne fût occupée qu'à parcourir le monde physique pour
ramasser les matériaux de ses connoissances, comme le botaniste qui
cueille ses végétaux, ou à extraire des principes de ses sensations,
comme le chimiste qui analyse les corps? Il étoit réservé à Locke de
nous donner sur les idées le vrai système de la nature, en développant
un principe connu par Aristote et saisi par Bacon, mais dont Locke n'est
pas moins le créateur, car un principe n'est créé que lorsqu'il est
démontré aux hommes. Qui nous démontrera de même ce que c'est que l'âme
des bêtes? quels sont ces êtres singuliers, si supérieurs aux végétaux
par leurs organes, si inférieurs à l'homme par leurs facultés? quel
est ce principe qui, sans leur donner la raison, produit en eux des
sensations, du mouvement et de la vie? Quelque parti que l'on embrasse,
la raison se trouble, la dignité de l'homme s'offense, ou la religion
s'épouvante. Chaque système est voisin d'une erreur; chaque route est
sur le bord d'un précipice. Ici Descartes est entraîné, par la force
des conséquences et l'enchaînement de ses idées, vers un système aussi
singulier que hardi, et qui est digne au moins de la grandeur de Dieu.
En effet, quelle idée plus sublime que de concevoir une multitude
innombrable de machines à qui l'organisation tient lieu de principe
intelligent; dont tous les ressorts sont différents, selon les
différentes espèces et les différents buts de la création; où tout est
prévu, tout combiné pour la conservation et la reproduction des êtres;
où toutes les opérations sont le résultat toujours sûr des lois du
mouvement; où toutes les causes qui doivent produire des millions
d'effets sont arrangées jusqu'à la fin des siècles, et ne dépendent que
de la correspondance et de l'harmonie de quelque partie de matière?
Avouons-le, ce système donne la plus grande idée de l'art de l'éternel
géomètre, comme l'appeloit Platon. C'est ce même caractère de grandeur
que l'on a retrouvé depuis dans l'harmonie préétablie de Leibnitz,
caractère plus propre que tout autre à séduire les hommes de génie, qui
aiment mieux voir tout en un instant dans une grande idée, que de se
traîner sur des détails d'observations et sur quelques vérités éparses
et isolées.
"""

# Affiche le nombre de mots dans le texte
nombre_de_mots = count_words(texte_1000_mots)
print(f"Nombre de mots dans le texte : {nombre_de_mots}")

# Liste prédéfinie de 256 symboles (caractères et bigrammes)
symboles_256 = [
    'b', 'j', '\r', 'J', '”', ')', 'Â', 'É', 'ê', '5', 't', '9', 'Y', '%', 'N', 'B', 'V', '\ufeff', 'Ê', '?', '’', 
    'i', ':', 's', 'C', 'â', 'ï', 'W', 'y', 'p', 'D', '—', '«', 'º', 'A', '3', 'n', '0', 'q', '4', 'e', 'T', 'È', '$', 
    'U', 'v', '»', 'l', 'P', 'X', 'Z', 'À', 'ç', 'u', '…', 'î', 'L', 'k', 'E', 'R', '2', '_', '8', 'é', 'O', 'Î', '‘', 
    'a', 'F', 'H', 'c', '[', '(', "'", 'è', 'I', '/', '!', ' ', '°', 'S', '•', '#', 'x', 'à', 'g', '*', 'Q', 'w', '1', 
    'û', '7', 'G', 'm', '™', 'K', 'z', '\n', 'o', 'ù', ',', 'r', ']', '.', 'M', 'Ç', '“', 'h', '-', 'f', 'ë', '6', ';', 
    'd', 'ô', 'e ', 's ', 't ', 'es', ' d', '\r\n', 'en', 'qu', ' l', 're', ' p', 'de', 'le', 'nt', 'on', ' c', ', ', 
    ' e', 'ou', ' q', ' s', 'n ', 'ue', 'an', 'te', ' a', 'ai', 'se', 'it', 'me', 'is', 'oi', 'r ', 'er', ' m', 'ce', 
    'ne', 'et', 'in', 'ns', ' n', 'ur', 'i ', 'a ', 'eu', 'co', 'tr', 'la', 'ar', 'ie', 'ui', 'us', 'ut', 'il', ' t', 
    'pa', 'au', 'el', 'ti', 'st', 'un', 'em', 'ra', 'e,', 'so', 'or', 'l ', ' f', 'll', 'nd', ' j', 'si', 'ir', 'e\r', 
    'ss', 'u ', 'po', 'ro', 'ri', 'pr', 's,', 'ma', ' v', ' i', 'di', ' r', 'vo', 'pe', 'to', 'ch', '. ', 've', 'nc', 
    'om', ' o', 'je', 'no', 'rt', 'à ', 'lu', "'e", 'mo', 'ta', 'as', 'at', 'io', 's\r', 'sa', "u'", 'av', 'os', ' à', 
    ' u', "l'", "'a", 'rs', 'pl', 'é ', '; ', 'ho', 'té', 'ét', 'fa', 'da', 'li', 'su', 't\r', 'ée', 'ré', 'dé', 'ec', 
    'nn', 'mm', "'i", 'ca', 'uv', '\n\r', 'id', ' b', 'ni', 'bl'
]

# Fonction pour déchiffrer le message
def decrypt(C):
    # Diviser le code en séquences de 8 bits
    sequences = [C[i:i+8] for i in range(0, len(C), 8)]
    
    # Calculer les fréquences des séquences
    sequence_counts = Counter(sequences)
    
    # Trouver les séquences les plus fréquentes
    most_common_sequences = sequence_counts.most_common()
    if len(most_common_sequences) < 2:
        print("Le code ne contient pas assez de séquences pour effectuer le décryptage.")
        return ""
    
    # Séquence la plus fréquente : espace, deuxième la plus fréquente : 's'
    espace_sequence = most_common_sequences[0][0]
    e_sequence = most_common_sequences[1][0]

    # Remplacer les séquences dans le code par les caractères correspondants
    code_decoded = C.replace(espace_sequence, ' ').replace(e_sequence, 's')
    
    # Retourner le message décrypté
    return code_decoded

# Exemple de code C
C = "1100111111010101011011000111010011001111000011100110110011001111110011000000110111001010010111010111111011001100011011001100111101101100011000011100111100001110011011001100111111001100000011011100101001011101011111101100110001101100011101001100111100001110011011001100111100111111000100100000011000111101000100100110110011001111011011000110000110010101000011000000111001101100110011110010000011001110011000010110110001110100110011110000111001101100110011110010000011001110011000010110110011001111011011000110000111001111000011100110110011001111001111110001001000000110001111010001001001101100011111001100111101011010001011011100101011001111011011001101010111001111"

# Appeler la fonction de décryptage et afficher le résultat
message_decrypte = decrypt(C)
print("\nMessage décrypté :")
print(message_decrypte)
##
## Voir document 2.py dans le GitHub ##
##
