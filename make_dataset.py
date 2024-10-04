## generate a simple dataset for clustering.
import random
import string

pos_lexicon = [
    "serendipity", "ephemeral", "luminous", "quixotic", "mellifluous", "effervescent", "ethereal", "nebula", "labyrinth", "cascade",
    "enigma", "velvet", "whisper", "zephyr", "opulent", "serenity", "quintessence", "enigmatic", "euphoria", "halcyon",
    "gossamer", "sublime", "eloquent", "epiphany", "sonorous", "surreptitious", "nebulous", "ineffable", "tranquil", "effulgent",
    "melancholy", "synchronicity", "paradox", "rhapsody", "zenith", "aurora", "sylvan", "efflorescent", "penumbra", "ardent",
    "epoch", "chrysalis", "ubiquitous", "labyrinthine", "soliloquy", "sanguine", "petrichor", "euphonious", "cerulean", "ebullient",
    "evanescent", "evocative", "exuberant", "felicity", "fenestration", "fidelity", "fleeting", "fortuitous", "gala", "harbinger",
    "harmony", "helix", "hiraeth", "horizont", "hypnotic", "idyllic", "illuminate", "illustrious", "imbue", "infinitesimal",
    "ingenue", "iridescent", "juxtapose", "kaleidoscope", "kismet", "lagom", "languor", "lilt", "liminal", "loquacious",
    "mercurial", "metamorphosis", "mirage", "mosaic", "murmur", "myriad", "nemesis", "nirvana", "nostalgia", "novella",
    "numinous", "oblivion", "oneiric", "opalescent", "panorama", "paragon", "panacea", "paradigm", "pastiche", "perennial",
    "perfection", "peripatetic", "phantasmagoria", "phenomenon", "piquant", "plethora", "poignant", "pristine", "prodigy", "radiant",
    "raconteur", "rapture", "recluse", "redolent", "resplendent", "reverie", "scintilla", "sojourn", "soporific", "subterfuge",
    "suerte", "sumptuous", "supine", "syzygy", "taciturn", "talisman", "tectonic", "tempestuous", "tenacious", "tessellate",
    "thalassic", "threnody", "timeless", "tourmaline", "translucent", "troubadour", "unctuous", "undulate", "unison", "utopia",
    "vagary", "velvety", "vesper", "vicissitude", "virtuoso", "vivacious", "wanderlust", "whimsical", "wisps", "xenial",
    "yonder", "zest", "abloom", "aesthetic", "allure", "amore", "apricity", "aquiver", "archipelago", "astonish",
    "aura", "beatific", "beguile", "beloved", "bewitch", "blossom", "bliss", "bloom", "bountiful", "breathtaking",
    "brilliance", "cadence", "celestial", "charm", "cherish", "chiaroscuro", "cinematic", "clandestine", "cognizant", "coalesce",
    "constellation", "crescendo", "cynosure", "dalliance", "dazzle", "delightful", "denouement", "diaphanous", "divine", "dulcet",
    "dusk", "eclat", "elation", "elixir", "elysian", "embellish", "embrace", "enchant", "epitome", "essence",
    "exquisite", "fascinate", "felicitous", "fervent", "flair", "flourish", "fortitude", "galvanize", "gleam", "glimmer",
    "grace", "grandiose", "harmonious", "haven", "illuminate", "incandescent", "infinite", "innate", "inspiration", "jubilant",
    "lagniappe", "lavish", "legacy", "leisure", "lilting", "limerence", "linger", "lullaby", "luminescent", "lustrous",
    "lyrical", "magnanimous", "mesmerize", "mirth", "muse", "oasis", "passion", "penchant", "poise", "propinquity",
    "ravishing", "sanguine", "scintillating", "serenade", "serene", "shimmering", "sincere", "solace", "soothe", "sparkling",
    "spectacle", "splendid", "supernal", "surreal", "symphony", "thrive", "traverse", "uplifting", "verve", "vivid",
    "wondrous", "aplomb", "august", "benevolent", "clement", "cozy", "enamor", "kinetic", "lush", "pastoral",
    "regal", "adamant", "adroit", "alacrity", "alchemy", "ambrosial", "amethyst", "amiable", "amity", "anachronism",
    "anecdote", "aplomb", "apotheosis", "arbiter", "arcane", "archetype", "ardor", "articulate", "august", "auspicious",
    "avatar", "avant-garde", "axiom", "beguile", "benevolent", "benign", "blithe", "bombastic", "bucolic", "cacophony",
    "capricious", "catharsis", "caustic", "charisma", "chivalrous", "clandestine", "clemency", "cogent", "cognizant", "colloquial",
    "combustible", "commensurate", "compelling", "compendium", "conciliatory", "congruent", "connoisseur", "consummate", "contentious", "convivial",
    "copious", "cordial", "coruscate", "cosset", "cosseted", "coterie", "countenance", "crepuscular", "crystalline", "curmudgeon",
    "dalliance", "debonair", "decadent", "delectable", "delineate", "denouement", "dexterous", "diaphanous", "didactic", "dilettante",
    "discerning", "dissonance", "dulcet", "ebb", "ebullient", "eclectic", "effervescent", "effusive", "elated", "eloquent",
    "elusive", "embellish", "embolden", "eminent", "empathy", "empirical", "enchant", "endemic", "enigmatic", "enlighten",
    "ennui", "ephemeral", "epiphany", "epitome", "equanimity", "erudite", "esoteric", "ethereal", "euphonious", "evanescent",
    "evocative", "exacerbate", "exalt", "exemplary", "exhilarate", "exotic", "expound", "exquisite", "extol", "exuberant",
    "facetious", "fastidious", "fathom", "fecund", "felicitous", "filigree", "finesse", "flabbergast", "flair", "flamboyant",
    "fluent", "flux", "fortuitous", "frenetic", "frisson", "frugal", "furtive", "gambit", "garrulous", "germane",
    "glib", "gossamer", "gregarious", "gumption", "halcyon", "harbinger", "hedonist", "hegemony", "hierarchy", "holistic",
    "hone", "hubris", "hyperbole", "iconoclast", "idiosyncratic", "idyllic", "ignite", "imbue", "immaculate", "immerse",
    "immutable", "impassioned", "impeccable", "imperious", "imperturbable", "impetuous", "implicit", "inalienable", "incessant", "incisive",
    "incandescent", "incognito", "incongruous", "indelible", "indolent", "ineffable", "ineluctable", "inextricable", "infallible", "ingenious",
    "ingenue", "ingenuity", "innocuous", "insatiable", "inscrutable", "insidious", "insolent", "intrepid", "intricate", "intrigue",
    "intuitive", "inveterate", "invigorate", "irascible", "iridescent", "irreverent", "jubilant", "juxtapose", "kismet", "labyrinth",
    "laconic", "lambent", "languid", "lascivious", "latent", "laud", "lethargic", "levity", "limpid", "loquacious",
    "lucid", "luminous", "lustrous", "magnanimous", "majestic", "malaise", "malinger", "malleable", "mellifluous", "mercurial",
    "meticulous", "milieu", "mitigate", "modicum", "monolithic", "myriad", "nadir", "nascent", "nefarious", "neophyte",
    "nonchalant", "nonplussed", "nostalgia", "notoriety", "novel", "nuance", "obfuscate", "oblique", "oblivion", "obscure",
    "obsolete", "obstinate", "obtain", "obviate", "occult", "octogenarian", "officious", "ominous", "onerous", "opaque",
    "opulent", "orator", "ostentatious", "ostracize", "overwhelm", "palatable", "palliate", "palpable", "panacea", "paradigm",
    "paradox", "paragon", "paramount", "pariah", "parsimonious", "passionate", "pastoral", "pathos", "paucity", "pedantic",
    "penchant", "penultimate", "perfidious", "perfunctory", "pernicious", "perpetuate", "pervasive", "petulant", "philanthropy", "phlegmatic",
    "picturesque", "piety", "piquant", "placate", "platitude", "plethora", "plummet", "poignant", "polarize", "pragmatic",
    "precarious", "precedent", "preclude", "precocious", "predilection", "preen", "prescient", "pretentious", "prevaricate", "primordial",
    "prodigal", "prodigious", "profuse", "prolific", "propensity", "propriety", "prosaic", "prosperity", "protean", "proximity",
    "prudent", "puerile", "pugnacious", "pulchritude", "punctilious", "pungent", "pyrrhic", "quagmire", "quandary", "quell",
    "querulous", "quintessential", "quixotic", "quotidian", "rancorous", "rarefy", "rational", "raucous", "raze", "rebuke",
    "recalcitrant", "recant", "recondite", "redolent", "refulgent", "regale", "relegate", "reminisce", "rendezvous", "renegade",
    "renounce", "repudiate", "resilient", "resplendent", "restive", "reticent", "revelry", "rhetoric", "rife", "riposte",
    "robust", "rudimentary", "ruminate", "sagacious", "sage", "salient", "salubrious", "sanguine", "sapient", "sartorial",
    "satiate", "saturate", "savor", "scandalous", "scintillating", "scrupulous", "serendipitous", "serene", "shrewd", "sinuous",
    "skeptical", "sojourn", "solace", "solicitous", "soliloquy", "soporific", "sordid", "sparse", "specious", "spendthrift",
    "spontaneous", "spurious", "squalid", "stagnant", "steadfast", "stoic", "strident", "stultify", "sublime", "submissive",
    "subterfuge", "subversive", "succinct", "superficial", "superfluous", "surreptitious", "sycophant", "symmetry", "synergy", "taciturn",
    "tangential", "tantamount", "tautology", "temerity", "tenacious", "tenuous", "terse", "thwart", "timorous", "tirade",
    "torpid", "torrid", "tractable", "tranquil", "transcend", "transient", "trepidation", "trite", "tumultuous", "ubiquitous",
    "unassailable", "uncanny", "unfathomable", "untenable", "unveil", "vacillate", "vacuous", "valor", "vapid", "variance",
    "vehement", "venerable", "verbose", "veritable", "versatile", "vestige", "vex", "vicarious", "vigilant", "vigorous",
    "virulent", "vital", "vivacious", "volatile", "voracious", "wane", "wary", "wax", "whimsical", "wistful",
    "zealous", "zenith", "zephyr", "zest"
]

neg_lexicon = [
    "abandon", "ability", "able", "about", "above", "absent", "absorb", "abstract", "absurd", "abuse",
    "access", "accident", "account", "accuse", "achieve", "acid", "acoustic", "acquire", "across", "act",
    "action", "actor", "actress", "actual", "adapt", "add", "addict", "address", "adjust", "admit",
    "adult", "advance", "advice", "aerobic", "affair", "afford", "afraid", "again", "age", "agent",
    "agree", "ahead", "aim", "air", "airport", "aisle", "alarm", "album", "alcohol", "alert",
    "alien", "all", "alley", "allow", "almost", "alone", "alpha", "already", "also", "alter",
    "always", "amateur", "amazing", "among", "amount", "amused", "analyst", "anchor", "ancient", "anger",
    "angle", "angry", "animal", "ankle", "announce", "annual", "another", "answer", "antenna", "antique",
    "anxiety", "any", "apart", "apology", "appear", "apple", "approve", "april", "arch", "arctic",
    "area", "arena", "argue", "arm", "armed", "armor", "army", "around", "arrange", "arrest",
    "arrive", "arrow", "art", "artefact", "artist", "artwork", "ask", "aspect", "assault", "asset",
    "assist", "assume", "asthma", "athlete", "atom", "attack", "attend", "attitude", "attract", "auction",
    "audit", "august", "aunt", "author", "auto", "autumn", "average", "avocado", "avoid", "awake",
    "aware", "away", "awesome", "awful", "awkward", "axis", "baby", "bachelor", "bacon", "badge",
    "bag", "balance", "balcony", "ball", "bamboo", "banana", "banner", "bar", "barely", "bargain",
    "barrel", "base", "basic", "basket", "battle", "beach", "bean", "beauty", "because", "become",
    "beef", "before", "begin", "behave", "behind", "believe", "below", "belt", "bench", "benefit",
    "best", "betray", "better", "between", "beyond", "bicycle", "bid", "bike", "bind", "biology",
    "bird", "birth", "bitter", "black", "blade", "blame", "blanket", "blast", "bleak", "bless",
    "blind", "blood", "blossom", "blouse", "blue", "blur", "blush", "board", "boat", "body",
    "boil", "bomb", "bone", "bonus", "book", "boost", "border", "boring", "borrow", "boss",
    "bottom", "bounce", "box", "boy", "bracket", "brain", "brand", "brass", "brave", "bread",
    "breeze", "brick", "bridge", "brief", "bright", "bring", "brisk", "broccoli", "broken", "bronze",
    "broom", "brother", "brown", "brush", "bubble", "buddy", "budget", "buffalo", "build", "bulb",
    "bulk", "bullet", "bundle", "bunker", "burden", "burger", "burst", "bus", "business", "busy",
    "butter", "buyer", "buzz", "cabbage", "cabin", "cable", "cactus", "cage", "cake", "call",
    "calm", "camera", "camp", "can", "canal", "cancel", "candy", "cannon", "canoe", "canvas",
    "canyon", "capable", "capital", "captain", "car", "carbon", "card", "cargo", "carpet", "carry",
    "cart", "case", "cash", "casino", "castle", "casual", "cat", "catalog", "catch", "category",
    "cattle", "caught", "cause", "caution", "cave", "ceiling", "celery", "cement", "census", "century",
    "cereal", "certain", "chair", "chalk", "champion", "change", "chaos", "chapter", "charge", "chase",
    "chat", "cheap", "check", "cheese", "chef", "cherry", "chest", "chicken", "chief", "child",
    "chimney", "choice", "choose", "chronic", "chuckle", "chunk", "churn", "cigar", "cinnamon", "circle",
    "citizen", "city", "civil", "claim", "clap", "clarify", "claw", "clay", "clean", "clerk",
    "clever", "click", "client", "cliff", "climb", "clinic", "clip", "clock", "clog", "close",
    "cloth", "cloud", "clown", "club", "clump", "cluster", "clutch", "coach", "coast", "coconut",
    "code", "coffee", "coil", "coin", "collect", "color", "column", "combine", "come", "comfort",
    "comic", "common", "company", "concert", "conduct", "confirm", "congress", "connect", "consider", "control",
    "convince", "cook", "cool", "copper", "copy", "coral", "core", "corn", "correct", "cost",
    "cotton", "couch", "country", "couple", "course", "cousin", "cover", "coyote", "crack", "cradle",
    "craft", "cram", "crane", "crash", "crater", "crawl", "crazy", "cream", "credit", "creek",
    "crew", "cricket", "crime", "crisp", "critic", "crop", "cross", "crouch", "crowd", "crucial",
    "cruel", "cruise", "crumble", "crunch", "crush", "cry", "crystal", "cube", "culture", "cup",
    "cupboard", "curious", "current", "curtain", "curve", "cushion", "custom", "cute", "cycle", "dad",
    "damage", "damp", "dance", "danger", "daring", "dash", "daughter", "dawn", "day", "deal",
    "debate", "debris", "decade", "december", "decide", "decline", "decorate", "decrease", "deer", "defense",
    "define", "defy", "degree", "delay", "deliver", "demand", "demise", "denial", "dentist", "deny",
    "depart", "depend", "deposit", "depth", "deputy", "derive", "describe", "desert", "design", "desk",
    "despair", "destroy", "detail", "detect", "develop", "device", "devote", "diagram", "dial", "diamond",
    "diary", "dice", "diesel", "diet", "differ", "digital", "dignity", "dilemma", "dinner", "dinosaur",
    "direct", "dirt", "disagree", "discover", "disease", "dish", "dismiss", "disorder", "display", "distance",
    "divert", "divide", "divorce", "dizzy", "doctor", "document", "dog", "doll", "dolphin", "domain",
    "donate", "donkey", "donor", "door", "dose", "double", "dove", "draft", "dragon", "drama",
    "drastic", "draw", "dream", "dress", "drift", "drill", "drink", "drip", "drive", "drop",
    "drum", "dry", "duck", "dumb", "dune", "during", "dust", "dutch", "duty", "dwarf",
    "dynamic", "eager", "eagle", "early", "earn", "earth", "easily", "east", "easy", "echo",
    "ecology", "economy", "edge", "edit", "educate", "effort", "egg", "eight", "either", "elbow",
    "elder", "electric", "elegant", "element", "elephant", "elevator", "elite", "else", "embark", "embody",
    "embrace", "emerge", "emotion", "employ", "empower", "empty", "enable", "enact", "end", "endless",
    "endorse", "enemy", "energy", "enforce", "engage", "engine", "enhance", "enjoy", "enlist", "enough",
    "enrich", "enroll", "ensure", "enter", "entire", "entry", "envelope", "episode", "equal", "equip",
    "era", "erase", "erode", "erosion", "error", "erupt", "escape", "essay", "essence", "estate",
    "eternal", "ethics", "evidence", "evil", "evoke", "evolve", "exact", "example", "excess", "exchange",
    "excite", "exclude", "excuse", "execute", "exercise", "exhaust", "exhibit", "exile", "exist", "exit",
    "exotic", "expand", "expect", "expire", "explain", "expose", "express", "extend", "extra", "eye",
    "eyebrow", "fabric", "face", "faculty", "fade", "faint", "faith", "fall", "false", "fame",
    "family", "famous", "fan", "fancy", "fantasy", "farm", "fashion", "fat", "fatal", "father",
    "fatigue", "fault", "favorite", "feature", "february", "federal", "fee", "feed", "feel", "female",
    "fence", "festival", "fetch", "fever", "few", "fiber", "fiction", "field", "figure", "file",
    "film", "filter", "final", "find", "fine", "finger", "finish", "fire", "firm", "first",
    "fiscal", "fish", "fit", "fitness", "fix", "flag", "flame", "flash", "flat", "flavor",
    "flee", "flight", "flip", "float", "flock", "floor", "flower", "fluid", "flush", "fly",
    "foam", "focus", "fog", "foil", "fold", "follow", "food", "foot", "force", "forest",
    "forget", "fork", "fortune", "forum", "forward", "fossil", "foster", "found", "fox", "fragile",
    "frame", "frequent", "fresh", "friend", "fringe", "frog", "front", "frost", "frown", "frozen",
    "fruit", "fuel", "fun", "funny", "furnace", "fury", "future", "gadget", "gain", "galaxy",
    "gallery", "game", "gap", "garage", "garbage", "garden", "garlic", "garment", "gas", "gasp",
    "gate", "gather", "gauge", "gaze", "general", "genius", "genre", "gentle", "genuine", "gesture",
    "ghost", "giant", "gift", "giggle", "ginger", "giraffe", "girl", "give", "glad", "glance",
    "glare", "glass", "glide", "glimpse", "globe", "gloom", "glory", "glove", "glow", "glue",
    "goat", "goddess", "gold", "good", "goose", "gorilla", "gospel", "gossip", "govern", "gown",
    "grab", "grace", "grain", "grant", "grape", "grass", "gravity", "great", "green", "grid",
    "grief", "grit", "grocery", "group", "grow", "grunt", "guard", "guess", "guide", "guilt",
    "guitar", "gun", "gym", "habit", "hair", "half", "hammer", "hamster", "hand", "happy",
    "harbor", "hard", "harsh", "harvest", "hat", "have", "hawk", "hazard", "head", "health",
    "heart", "heavy", "hedgehog", "height", "hello", "helmet", "help", "hen", "hero", "hidden",
    "high", "hill", "hint", "hip", "hire", "history", "hobby", "hockey", "hold", "hole",
    "holiday", "hollow", "home", "honey", "hood", "hope", "horn", "horror", "horse", "hospital",
    "host", "hotel", "hour", "hover", "hub", "huge", "human", "humble", "humor", "hundred",
    "hungry", "hunt", "hurdle", "hurry", "hurt", "husband", "hybrid", "ice", "icon", "idea",
    "identify", "idle", "ignore", "ill", "illegal", "illness", "image", "imitate", "immense", "immune",
    "impact", "impose", "improve", "impulse", "inch", "include", "income", "increase", "index", "indicate",
    "indoor", "industry", "infant", "inflict", "inform", "inhale", "inherit", "initial", "inject", "injury",
    "inmate", "inner", "innocent", "input", "inquiry", "insane", "insect", "inside", "inspire", "install",
    "intact", "interest", "into", "invest", "invite", "involve", "iron", "island", "isolate", "issue",
    "item", "ivory", "jacket", "jaguar", "jar", "jazz", "jealous", "jeans", "jelly", "jewel",
    "job", "join", "joke", "journey", "joy", "judge", "juice", "jump", "jungle", "junior",
    "junk", "just", "kangaroo", "keen", "keep", "ketchup", "key", "kick", "kid", "kidney",
    "kind", "kingdom", "kiss", "kit", "kitchen", "kite", "kitten", "kiwi", "knee", "knife",
    "knock", "know", "lab", "label", "labor", "ladder", "lady", "lake", "lamp", "language",
    "laptop", "large", "later", "latin", "laugh", "laundry", "lava", "law", "lawn", "lawsuit",
    "layer", "lazy", "leader", "leaf", "learn", "leave", "lecture", "left", "leg", "legal"
]

def create_docs(npos, nneg) :
    length = 100
    stopwords = ['a', 'an', 'the']
    pos_docs = []
    neg_docs = []
    for i in range(npos) :
        if random.random() < 0.2:
            word = random.choice(stopwords)
        else:
            word = random.choice(pos_lexicon)
        if random.random() < 0.2:
            word = word.capitalize()
        if random.random() < 0.3:
            word += random.choice(string.punctuation)
        d = [word for j in range(length)]
        pos_docs.append(d)

    for j in range(nneg) :
        if random.random() < 0.2:
            word = random.choice(stopwords)
        else:
            word = random.choice(pos_lexicon)
        if random.random() < 0.2:
            word = word.capitalize()
        if random.random() < 0.3:
            word += random.choice(string.punctuation)
        d = [word for j in range(length)]
        neg_docs.append(d)

    return (pos_docs, neg_docs)