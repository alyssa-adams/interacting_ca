import re

text = """
Undecidability and indeterminism by Klaas Landsman
52 posts  •  created by Klaas Landsman   •  Mar. 7, 2020 @ 21:09 GMT
Community Rating: 7.7 (17 ratings)   Public Rating: N/A

Undecidability and unpredictability: not limitations, but triumphs of science by Markus P Mueller
40 posts  •  created by Markus P Mueller   •  Apr. 21, 2020 @ 11:12 GMT
Community Rating: 7.7 (25 ratings)   Public Rating: N/A

Indeterminism, causality and information: Has physics ever been deterministic? by Flavio Del Santo
149 posts  •  created by Flavio Del Santo   •  Mar. 11, 2020 @ 16:10 GMT
Community Rating: 7.6 (44 ratings)   Public Rating: 9.2 (9 ratings)

Undecidability, Fractal Geometry and the Unity of Physics by Tim Palmer
79 posts  •  created by Tim Palmer   •  Jan. 25, 2020 @ 17:48 GMT
Community Rating: 7.5 (29 ratings)   Public Rating: 5.0 (4 ratings)

Sentience, the ontology of experience by Cristinel Stoica
92 posts  •  created by Cristinel Stoica   •  Apr. 13, 2020 @ 11:23 GMT
Community Rating: 7.4 (21 ratings)   Public Rating: N/A

Restoration of predictability in gravitational collapse by Christian Corda
69 posts  •  created by Christian Corda   •  Jan. 7, 2020 @ 17:54 GMT
Community Rating: 7.4 (18 ratings)   Public Rating: 8.0 (4 ratings)

Epistemic Horizons: This Sentence is 1/√2(|True> + |False>) by Jochen Szangolies
112 posts  •  created by Jochen Szangolies   •  Jan. 27, 2020 @ 23:28 GMT
Community Rating: 7.2 (29 ratings)   Public Rating: 6.6 (5 ratings)

Deciding on the nature of time and space by Edwin Eugene Klingman
137 posts  •  created by Edwin Eugene Klingman   •  Apr. 3, 2020 @ 01:20 GMT
Community Rating: 7.2 (23 ratings)   Public Rating: 8.0 (2 ratings)

Mutual Explainability, or, a Comedy in Computerland by Simon DeDeo
18 posts  •  created by Simon DeDeo   •  Apr. 19, 2020 @ 22:21 GMT
Community Rating: 7.2 (6 ratings)   Public Rating: 7.0 (2 ratings)

Dialectical-Ontological Modeling of Primordial Generating Process ↔ Understand λόγος ↔Δ↔Logos & Count Quickly↔Ontological (Cosmic, Structural) Memory by Vladimir I. Rogozhin
60 posts  •  created by Vladimir Rogozhin   •  Mar. 5, 2020 @ 12:05 GMT
Community Rating: 7.1 (22 ratings)   Public Rating: 8.2 (5 ratings)

The Uncertain Future of Physics and Computing by Alan M. Kadin
46 posts  •  created by Alan M. Kadin   •  Mar. 13, 2020 @ 16:15 GMT
Community Rating: 7.1 (14 ratings)   Public Rating: 7.3 (7 ratings)

Noisy Machines by Michael James Kewming
27 posts  •  created by Michael James Kewming   •  Apr. 22, 2020 @ 20:21 GMT
Community Rating: 7.1 (15 ratings)   Public Rating: 8.0 (1 rating)

Of universal computers, infinities, and demons by Rafael Alves Batista
16 posts  •  created by Rafael Alves Batista   •  Apr. 24, 2020 @ 13:40 GMT
Community Rating: 7.0 (8 ratings)   Public Rating: 8.3 (4 ratings)

Why is the universe comprehensible? by Ian Durham
47 posts  •  created by Ian Durham   •  Apr. 25, 2020 @ 15:01 GMT
Community Rating: 7.0 (13 ratings)   Public Rating: N/A

Physics and science: the art of taking a stance about undecidable questions by Fabien Paillusson
35 posts  •  created by Fabien Paillusson   •  Apr. 9, 2020 @ 10:50 GMT
Community Rating: 7.0 (8 ratings)   Public Rating: 8.8 (6 ratings)

The subtle sound of quantum jumps by Antoine Tilloy
11 posts  •  created by Antoine Tilloy Tilloy   •  Mar. 23, 2020 @ 01:11 GMT
Community Rating: 7.0 (6 ratings)   Public Rating: N/A

Unverifiability, Unexplainability & Unpredictability by Roman V Yampolskiy
24 posts  •  created by Roman V Yampolskiy   •  Jan. 28, 2020 @ 16:47 GMT
Community Rating: 7.0 (13 ratings)   Public Rating: 7.0 (9 ratings)

A Gödelian Hunch from Quantum Theory by Hippolyte Dourdent
20 posts  •  created by Hippolyte Dourdent   •  Apr. 24, 2020 @ 00:31 GMT
Community Rating: 6.9 (11 ratings)   Public Rating: 9.7 (6 ratings)

Unpredictable Random Number Generator by Yutaka Shikano
29 posts  •  created by Yutaka Shikano   •  Mar. 9, 2020 @ 22:45 GMT
Community Rating: 6.9 (9 ratings)   Public Rating: 4.5 (2 ratings)

Math Matters by Sabine Hossenfelder
66 posts  •  created by Sabine Hossenfelder   •  Mar. 11, 2020 @ 01:23 GMT
Community Rating: 6.9 (40 ratings)   Public Rating: 6.5 (8 ratings)

Interpreting Quantum Mechanics and Predictability in Terms of Facts About the Universe by Andrew Knight
27 posts  •  created by Andrew Knight   •  Mar. 22, 2020 @ 01:37 GMT
Community Rating: 6.8 (13 ratings)   Public Rating: N/A

Does God play dice with time itself? by Del Rajan
21 posts  •  created by Del Rajan   •  Apr. 24, 2020 @ 14:26 GMT
Community Rating: 6.8 (12 ratings)   Public Rating: N/A

Universality Everywhere implies Undecidability Everywhere by Gemma De las Cuevas
13 posts  •  created by Gemma De las Cuevas   •  Apr. 24, 2020 @ 17:19 GMT
Community Rating: 6.7 (11 ratings)   Public Rating: N/A

The Mind and the Limitations of Physics by Noson S. Yanofsky
36 posts  •  created by Noson S. Yanofsky   •  Mar. 1, 2020 @ 12:59 GMT
Community Rating: 6.7 (12 ratings)   Public Rating: N/A

On the Origin of Quantum Uncertainty by Chris Adami
11 posts  •  created by Chris Adami   •  Apr. 19, 2020 @ 11:21 GMT
Community Rating: 6.6 (8 ratings)   Public Rating: N/A

Mathematics is Physical by Sara Walker
21 posts  •  created by Sara Walker   •  Apr. 25, 2020 @ 17:46 GMT
Community Rating: 6.6 (18 ratings)   Public Rating: 5.0 (1 rating)

Learning from Theories by Michael Dascal
21 posts  •  created by Michael Dascal   •  Apr. 25, 2020 @ 01:32 GMT
Community Rating: 6.6 (15 ratings)   Public Rating: N/A

Blondes, Brunettes & the Flaw of the Excluded Middle by Peter Jackson
103 posts  •  created by Peter Jackson   •  Feb. 18, 2020 @ 22:20 GMT
Community Rating: 6.6 (24 ratings)   Public Rating: 6.7 (3 ratings)

Deep Incompleteness: What Laplace's Demon Doesn't Know by Dean Rickles
9 posts  •  created by Dean Rickles   •  Mar. 20, 2020 @ 14:04 GMT
Community Rating: 6.6 (7 ratings)   Public Rating: N/A

Can Brazilian butterfly flaps destroy the universe? How fundamental limits on knowledge and computation force Laplace's demon to become a scientist by John Joseph Vastola
32 posts  •  created by John Joseph Vastola   •  Apr. 24, 2020 @ 00:30 GMT
Community Rating: 6.5 (11 ratings)   Public Rating: 7.7 (3 ratings)

LOST IN MATH... AND MEASUREMENTS by Israel Perez
60 posts  •  created by Israel Perez   •  Apr. 3, 2020 @ 14:42 GMT
Community Rating: 6.5 (14 ratings)   Public Rating: 7.0 (1 rating)

A Framework for Thinking about Knowability by John S Schultz
26 posts  •  created by John S Schultz   •  Apr. 9, 2020 @ 10:50 GMT
Community Rating: 6.5 (8 ratings)   Public Rating: 7.5 (2 ratings)

Noisy Deductive Reasoning: How Humans Construct Math, and How Math Constructs Universes by David H. Wolpert
23 posts  •  created by David B Kinney   •  Apr. 25, 2020 @ 17:48 GMT
Community Rating: 6.5 (14 ratings)   Public Rating: 7.8 (4 ratings)

Scientific Determinism-A Case for Human Cognitive Selection Bias by Michael Muteru
25 posts  •  created by Michael muteru   •  Apr. 24, 2020 @ 14:13 GMT
Community Rating: 6.5 (17 ratings)   Public Rating: 9.3 (3 ratings)

Metadynamics by Christine Cordula Dantas
28 posts  •  created by Christine Cordula Dantas   •  Feb. 27, 2020 @ 19:08 GMT
Community Rating: 6.5 (11 ratings)   Public Rating: N/A

Positivist perspective on predictability by Roger Schlafly
27 posts  •  created by Roger Schlafly   •  Mar. 20, 2020 @ 14:03 GMT
Community Rating: 6.5 (11 ratings)   Public Rating: 4.0 (2 ratings)

*On The Limits of Deducibility* by Stefan Weckbach
28 posts  •  created by Stefan Weckbach   •  Mar. 20, 2020 @ 14:04 GMT
Community Rating: 6.4 (9 ratings)   Public Rating: N/A

The pollen and the electron: a study in randomness by Tejinder P. Singh
16 posts  •  created by Tejinder Pal Singh   •  Apr. 22, 2020 @ 20:25 GMT
Community Rating: 6.4 (7 ratings)   Public Rating: N/A

No single unification theory of everything by Wanpeng Tan
30 posts  •  created by Wanpeng Tan   •  Mar. 5, 2020 @ 12:08 GMT
Community Rating: 6.4 (7 ratings)   Public Rating: N/A

Undecidability of States and Epistemic Horizons as Quantum Gravity by Lawrence B. Crowell
57 posts  •  created by Lawrence B. Crowell   •  Feb. 11, 2020 @ 01:09 GMT
Community Rating: 6.4 (13 ratings)   Public Rating: N/A

Putting the 'Pre' in 'Unpredictability' by Emily Christine Adlam
31 posts  •  created by Emily Christine Adlam   •  Mar. 16, 2020 @ 16:44 GMT
Community Rating: 6.4 (8 ratings)   Public Rating: N/A

Logics with a Future by Mozibur Rahman Ullah
18 posts  •  created by Mozibur Rahman Ullah   •  Apr. 25, 2020 @ 01:32 GMT
Community Rating: 6.4 (8 ratings)   Public Rating: N/A

What is Beyond Reckoning? by Jonathan J. Dickau
90 posts  •  created by Jonathan J. Dickau   •  Jan. 28, 2020 @ 22:40 GMT
Community Rating: 6.3 (15 ratings)   Public Rating: N/A

Contradictions Between Quantum Mechanics and Conventional Physics Laws of Nature by Ronald Racicot
29 posts  •  created by Ronald Racicot   •  Feb. 29, 2020 @ 18:27 GMT
Community Rating: 6.3 (6 ratings)   Public Rating: N/A

The transformation of uncertainty into certainty. The relationship of the Lorentz factor with the probability density of states. And more from a new Cartesian generalization of modern physics. by Dizhechko Boris Semyonovich
26 posts  •  created by Dizhechko Boris Semyonovich   •  Jan. 13, 2020 @ 16:42 GMT
Community Rating: 6.3 (15 ratings)   Public Rating: N/A

A properly deciding, Computing and Predicting new theory’s Philosophy by Satyavarapu Naga Parameswara Gupta
115 posts  •  created by Satyavarapu Naga Parameswara Gupta   •  Mar. 1, 2020 @ 14:37 GMT
Community Rating: 6.3 (25 ratings)   Public Rating: 7.8 (20 ratings)

An Undecidable Universe by Paul Davies
17 posts  •  created by Paul Davies   •  Apr. 24, 2020 @ 13:36 GMT
Community Rating: 6.3 (13 ratings)   Public Rating: N/A

On the Decidability of Determinism and Time’s Arrow by Harrison Crecraft
21 posts  •  created by Harrison Crecraft   •  Feb. 13, 2020 @ 11:19 GMT
Community Rating: 6.3 (7 ratings)   Public Rating: 5.0 (1 rating)

Objectivity and Time by Ronald Green
22 posts  •  created by Ronald Green   •  Mar. 12, 2020 @ 14:49 GMT
Community Rating: 6.3 (7 ratings)   Public Rating: 4.5 (2 ratings)

Calculate “as if “… but be careful by Eckard Blumschein
87 posts  •  created by Eckard Blumschein   •  Feb. 4, 2020 @ 18:05 GMT
Community Rating: 6.3 (11 ratings)   Public Rating: 5.5 (2 ratings)

Wandering towards a ‘Theory of Everything’ and how I was stopped from achieving my goal by Nature by Lachlan Cresswell
31 posts  •  created by Lachlan Cresswell   •  Feb. 17, 2020 @ 12:06 GMT
Community Rating: 6.3 (11 ratings)   Public Rating: 9.0 (2 ratings)

Unpredictable, yet Physically Meaningful: Insights into the Boundary between Observer and Obseved by William C. McHarris
18 posts  •  created by William C. McHarris   •  Mar. 4, 2020 @ 02:37 GMT
Community Rating: 6.3 (8 ratings)   Public Rating: N/A

PHYSICS AND UUU - BASED MATHEMATICAL PROBLEMS by Michael Alexeevich Popov
9 posts  •  created by Michael Alexeevich Popov   •  Mar. 11, 2020 @ 01:24 GMT
Community Rating: 6.3 (4 ratings)   Public Rating: N/A

THE COMPLETELY UNKNOWN by Wilhelmus de Wilde
36 posts  •  created by Wilhelmus de Wilde de Wilde   •  Feb. 29, 2020 @ 18:27 GMT
Community Rating: 6.2 (13 ratings)   Public Rating: 7.3 (3 ratings)

Incompleteness, Entropy and Unification by Boris Egorov
11 posts  •  created by Boris Egorov   •  Apr. 10, 2020 @ 12:57 GMT
Community Rating: 6.2 (5 ratings)   Public Rating: N/A

The Door That Has No Key by George Gantz
15 posts  •  created by George Gantz   •  Apr. 20, 2020 @ 10:38 GMT
Community Rating: 6.2 (5 ratings)   Public Rating: N/A

Do the 3 "Uns" have it? by James Lee Hoover
29 posts  •  created by James Lee Hoover   •  Feb. 14, 2020 @ 00:19 GMT
Community Rating: 6.2 (16 ratings)   Public Rating: 9.0 (1 rating)

On the Deterministic Roots of Indeterminacy by Terry Bollinger
21 posts  •  created by Terry Bollinger   •  Apr. 25, 2020 @ 14:57 GMT
Community Rating: 6.2 (6 ratings)   Public Rating: N/A

Logic, Formalism and Reality by Mihai C Panoschi
14 posts  •  created by Mihai Panoschi Panoschi   •  Mar. 5, 2020 @ 12:06 GMT
Community Rating: 6.1 (7 ratings)   Public Rating: 5.0 (3 ratings)

Mathematics, Shaken but not Stirred by Kevin H Knuth
24 posts  •  created by Kevin H Knuth   •  Apr. 25, 2020 @ 17:30 GMT
Community Rating: 6.1 (12 ratings)   Public Rating: 10.0 (1 rating)

Semantically Closed Theories and the Unpredictable Evolution of the Laws of Physics by Luca Valeri
29 posts  •  created by Luca Valeri   •  Apr. 25, 2020 @ 17:45 GMT
Community Rating: 6.1 (12 ratings)   Public Rating: 9.0 (3 ratings)

From Unpredictability to Predictability by Branko L Zivlak
53 posts  •  created by Branko L Zivlak   •  Jan. 20, 2020 @ 11:55 GMT
Community Rating: 6.1 (12 ratings)   Public Rating: 4.5 (2 ratings)

Asymmetry of Time Symmetry by Eric Aspling
8 posts  •  created by Eric Aspling   •  Mar. 11, 2020 @ 16:09 GMT
Community Rating: 6.0 (4 ratings)   Public Rating: 4.0 (2 ratings)

Determinancy becomes unpredictable, uncomputable and undecidable by Bruce E Camber
9 posts  •  created by Bruce E Camber   •  Mar. 8, 2020 @ 17:03 GMT
Community Rating: 6.0 (4 ratings)   Public Rating: 9.0 (1 rating)

A dialogue concerning undecidability, uncomputability and unpredictability by Gabriele Carcassi
12 posts  •  created by Gabriele Carcassi   •  Apr. 18, 2020 @ 12:03 GMT
Community Rating: 6.0 (4 ratings)   Public Rating: N/A

UNDECIDABILITY, UNCOMPUTABILITY AND UNPREDICTABILITY: Paradigmatic Reflections in the Space of Classical-Fuzzy Logical Duality by KOFI KISSI DOMPERE
5 posts  •  created by KOFI KISSI DOMPERE   •  Mar. 7, 2020 @ 21:10 GMT
Community Rating: 6.0 (3 ratings)   Public Rating: N/A

Universal quantum laws of the universe to solve the problems of unsolvability, computability and unpredictability by Vladimir Nikolaevich Fedorov
15 posts  •  created by Vladimir Nikolaevich Fedorov   •  Apr. 3, 2020 @ 01:22 GMT
Community Rating: 6.0 (5 ratings)   Public Rating: N/A

Laplace's Demon -- Thwarted by Modern Physics, or Does He Know Something We Don't? by Stephen Klein
12 posts  •  created by Stephen Klein   •  Apr. 25, 2020 @ 15:08 GMT
Community Rating: 6.0 (7 ratings)   Public Rating: N/A

Contradictions, mathematical science and incompleteness by Abhishek Majhi
11 posts  •  created by Abhishek Majhi   •  Apr. 7, 2020 @ 14:53 GMT
Community Rating: 6.0 (4 ratings)   Public Rating: 8.0 (1 rating)

World-Universe Model – Alternative to Big Bang Model by Vladimir Netchitailo
3 posts  •  created by Vladimir Netchitailo   •  Apr. 15, 2020 @ 01:18 GMT
Community Rating: 6.0 (3 ratings)   Public Rating: 10.0 (1 rating)

Mathematics: The Epistemic Veil Clothing Nature by Syed Raiyan Nuri Reza
25 posts  •  created by Syed Raiyan Nuri Reza   •  Apr. 25, 2020 @ 17:35 GMT
Community Rating: 6.0 (8 ratings)   Public Rating: N/A

Un-decidability Implies Alternatives Exist. by Paul Schroeder
29 posts  •  created by Paul Schroeder   •  Feb. 2, 2020 @ 23:58 GMT
Community Rating: 6.0 (8 ratings)   Public Rating: N/A

An Open-ended Quantum Universe by Tatsu Takeuchi
8 posts  •  created by Tatsu Takeuchi   •  May. 5, 2020 @ 20:09 GMT
Community Rating: 6.0 (7 ratings)   Public Rating: N/A

A Grand Introduction to Darwinian Mechanics by Kwame A Bennett
21 posts  •  created by Kwame A Bennett   •  Apr. 25, 2020 @ 12:00 GMT
Community Rating: 5.9 (12 ratings)   Public Rating: 10.0 (8 ratings)

Adapt Mathematics to Science, Not Science to Mathematics by Scott Guthery
23 posts  •  created by Scott Guthery   •  Mar. 31, 2020 @ 16:56 GMT
Community Rating: 5.9 (10 ratings)   Public Rating: 6.0 (2 ratings)

Embracing undecidability: Cognitive needs and theory evaluation by André C. R. Martins
15 posts  •  created by André C. R. Martins   •  Feb. 10, 2020 @ 12:39 GMT
Community Rating: 5.9 (10 ratings)   Public Rating: 6.3 (3 ratings)

An Introduction to Grand Unification by Antoine E Pinnock
10 posts  •  created by Antoine E Pinnock   •  Jan. 18, 2020 @ 12:45 GMT
Community Rating: 5.9 (8 ratings)   Public Rating: 7.0 (3 ratings)

Je suis, nous sommes Wigner! A perspectival exploration of the Frauchiger–Renner paradox by Malcolm Riddoch
20 posts  •  created by Malcolm Riddoch   •  Apr. 25, 2020 @ 17:36 GMT
Community Rating: 5.9 (8 ratings)   Public Rating: 8.0 (1 rating)

Well Beyond Uncertainty, Uncomputability, and Unpredictability by Daniel Sudarsky
10 posts  •  created by Daniel Sudarsky   •  Apr. 24, 2020 @ 13:28 GMT
Community Rating: 5.9 (7 ratings)   Public Rating: N/A

The Cosmological Cheshire Cat -- Predictable and Unpredictable Dark Matter Properties by Jenny Wagner
13 posts  •  created by Jenny Wagner   •  Apr. 23, 2020 @ 12:07 GMT
Community Rating: 5.9 (7 ratings)   Public Rating: 9.3 (4 ratings)

Is the aether undecidable? by Marts Liena
19 posts  •  created by Marts Liena   •  Mar. 31, 2020 @ 16:56 GMT
Community Rating: 5.8 (5 ratings)   Public Rating: 7.0 (1 rating)

Completeness of System by Ilgaitis Prusis
17 posts  •  created by Ilgaitis Prusis   •  Apr. 23, 2020 @ 12:10 GMT
Community Rating: 5.8 (5 ratings)   Public Rating: N/A

Unpredictable unpredictables by Robert Wilson
34 posts  •  created by Robert Wilson   •  Mar. 30, 2020 @ 15:14 GMT
Community Rating: 5.8 (5 ratings)   Public Rating: 7.0 (2 ratings)

Remembering the Future by Yehonatan Knoll
19 posts  •  created by Yehonatan Knoll   •  Feb. 17, 2020 @ 17:59 GMT
Community Rating: 5.8 (9 ratings)   Public Rating: N/A

Gödel versus Wolfram on Undecidability, Uncomputability, and Unpredictability, plus Bohr versus Einstein on Uncertainty by David Brown
91 posts  •  created by David Brown   •  Jan. 7, 2020 @ 17:54 GMT
Community Rating: 5.8 (8 ratings)   Public Rating: N/A

Self-Assembling Universes Maximize Novelty by Leroy Cronin
7 posts  •  created by Leroy Cronin   •  Apr. 25, 2020 @ 11:52 GMT
Community Rating: 5.8 (12 ratings)   Public Rating: 7.0 (2 ratings)

Computability in the Theory of Theories by Philip Gibbs
71 posts  •  created by Philip Gibbs   •  Feb. 19, 2020 @ 15:57 GMT
Community Rating: 5.8 (8 ratings)   Public Rating: N/A

Modeling Universal Intelligence by Sue Lingo
18 posts  •  created by Sue Lingo   •  Apr. 13, 2020 @ 11:23 GMT
Community Rating: 5.8 (4 ratings)   Public Rating: 7.5 (2 ratings)

Unpredictability and Randomness by Rade Vuckovac
7 posts  •  created by Rade Vuckovac   •  Apr. 23, 2020 @ 12:08 GMT
Community Rating: 5.8 (4 ratings)   Public Rating: N/A

THE UNDECIDABILITY OF THE EPR PARADOX IS RESOLVED by barry gilbert
9 posts  •  created by barry gilbert   •  Apr. 23, 2020 @ 19:08 GMT
Community Rating: 5.7 (7 ratings)   Public Rating: 7.5 (2 ratings)

Sources of Unpredictability in Quantum Mechanics by Alireza Jamali
11 posts  •  created by Alireza Jamali   •  Jan. 16, 2020 @ 14:41 GMT
Community Rating: 5.7 (7 ratings)   Public Rating: N/A

Who Wants to be a Millionaire? A Guide to Computing Complex Systems by Alyssa Adams
15 posts  •  created by Alyssa Adams   •  Apr. 25, 2020 @ 11:54 GMT
Community Rating: 5.7 (10 ratings)   Public Rating: 9.0 (1 rating)

How to obtain a mass of a graviton. Does our formulation lead to Undecidability, Uncomputability, and Unpredictability issues ? What are the implications of such Issues ? by andrew beckwith
54 posts  •  created by Andrew Beckwith   •  Apr. 10, 2020 @ 12:56 GMT
Community Rating: 5.7 (6 ratings)   Public Rating: N/A

Resolving the Unknown Universe by Stephen Harold Jarvis
8 posts  •  created by Stephen Jarvis   •  Apr. 3, 2020 @ 14:41 GMT
Community Rating: 5.7 (3 ratings)   Public Rating: N/A

Predictable and un-Predictable in the Universe and the Mind by Michael Patrick Bradley
4 posts  •  created by Michael Patrick Bradley   •  Apr. 25, 2020 @ 14:58 GMT
Community Rating: 5.6 (5 ratings)   Public Rating: N/A

Limits of human knowledge by John C Hodge
25 posts  •  created by John C Hodge   •  Feb. 8, 2020 @ 11:14 GMT
Community Rating: 5.6 (10 ratings)   Public Rating: N/A

Unravelling the Missing Physics behind Undecidability, Uncomputability, and Unpredictability by Avtar Singh
18 posts  •  created by Avtar Singh   •  Mar. 12, 2020 @ 14:50 GMT
Community Rating: 5.6 (5 ratings)   Public Rating: N/A

Computational Complexity as Anthropic Principle by Rick Searle
8 posts  •  created by Rick Searle   •  Mar. 15, 2020 @ 19:55 GMT
Community Rating: 5.6 (7 ratings)   Public Rating: N/A

Undecidability, Uncomputability, and Unpredictability - There is no Brave New World anymore! by Torsten Asselmeyer-Maluga
9 posts  •  created by Torsten Asselmeyer-Maluga   •  Apr. 24, 2020 @ 14:11 GMT
Community Rating: 5.5 (6 ratings)   Public Rating: 9.3 (4 ratings)

Wishful Thinking: the Resurrection of Laplace Demon by BASILEIOS GRISPOS
13 posts  •  created by BASILEIOS GRISPOS   •  Mar. 7, 2020 @ 21:09 GMT
Community Rating: 5.5 (4 ratings)   Public Rating: 7.0 (6 ratings)

Minkowski spacetime - a no-go for objective becoming by Vesselin Petkov
21 posts  •  created by Vesselin Petkov   •  Apr. 15, 2020 @ 13:13 GMT
Community Rating: 5.5 (6 ratings)   Public Rating: N/A

In QFT veritas, in Pyrex sanitas by Alan M. Schwartz
19 posts  •  created by Alan M. Schwartz   •  Feb. 4, 2020 @ 01:57 GMT
Community Rating: 5.5 (8 ratings)   Public Rating: 9.0 (1 rating)

Measurability and Computability of the Universe by Amrit Srecko Sorli
27 posts  •  created by Amrit Srecko Sorli   •  Feb. 23, 2020 @ 17:37 GMT
Community Rating: 5.5 (6 ratings)   Public Rating: N/A

Category Mistakes and Time Traps by H.H.J. Luediger
14 posts  •  created by H.H.J. Luediger   •  Feb. 10, 2020 @ 12:40 GMT
Community Rating: 5.4 (7 ratings)   Public Rating: N/A

RANDOMNESS, COMPUTABILITY, AND EMBODIMENT by Dan J. Bruiger
9 posts  •  created by Dan J. Bruiger   •  Feb. 29, 2020 @ 18:28 GMT
Community Rating: 5.4 (5 ratings)   Public Rating: N/A

An artist's perspective on paradox. by John Philip Clive
10 posts  •  created by John Philip Clive   •  Apr. 24, 2020 @ 14:55 GMT
Community Rating: 5.4 (5 ratings)   Public Rating: 8.0 (1 rating)

Unsolvability in the Anthropocene by Nathan L. Harshman
6 posts  •  created by Nathan L. Harshman   •  Apr. 25, 2020 @ 15:06 GMT
Community Rating: 5.4 (5 ratings)   Public Rating: N/A

Why your robot is just not that into you by Jeffrey Michael Schmitz
8 posts  •  created by Jeffrey Michael Schmitz   •  Apr. 24, 2020 @ 13:32 GMT
Community Rating: 5.4 (5 ratings)   Public Rating: N/A

To Be or Not to Be? But is that really the Question? by Jason W Steinmetz
16 posts  •  created by Jason W Steinmetz   •  Apr. 25, 2020 @ 17:41 GMT
Community Rating: 5.4 (10 ratings)   Public Rating: N/A

The Outcomes of Logical Analysis Are Unpredictable by Lorraine Ford
29 posts  •  created by Lorraine Ford   •  Mar. 8, 2020 @ 01:22 GMT
Community Rating: 5.3 (6 ratings)   Public Rating: N/A

Nature Remains Behind the Veil: Superluminal Signaling Fails to Credibly Explain Strong Correlations by Neil Bates
5 posts  •  created by Neil Bates   •  Apr. 25, 2020 @ 11:59 GMT
Community Rating: 5.3 (4 ratings)   Public Rating: N/A

Clarification of Physics: A Derivation of a Complete, Computable, Predictive Model of “Our” Multiverse. by John David Crowell
49 posts  •  created by John David Crowell   •  Mar. 12, 2020 @ 14:48 GMT
Community Rating: 5.3 (8 ratings)   Public Rating: 7.0 (3 ratings)

New ontology: algorithmic laws and the passage of time by Pavel Vadimovich Poluian
9 posts  •  created by Pavel Vadimovich Poluian   •  Apr. 23, 2020 @ 13:08 GMT
Community Rating: 5.3 (4 ratings)   Public Rating: 10.0 (1 rating)

Incompleteness Implications for a Theory of Everything by Donald G Palmer
5 posts  •  created by Donald G Palmer   •  Feb. 23, 2020 @ 17:37 GMT
Community Rating: 5.2 (5 ratings)   Public Rating: N/A

Barber or not barber? by Domenico Oricchio
17 posts  •  created by Domenico Oricchio   •  Jan. 7, 2020 @ 17:54 GMT
Community Rating: 5.1 (7 ratings)   Public Rating: 2.0 (1 rating)

THE UNKNOWABLE BORDERS THE UNKNOWN - A threefold limit to our knowledge by Paolo Bellan
2 posts  •  created by Paolo Bellan   •  Apr. 24, 2020 @ 14:54 GMT
Community Rating: 5.0 (2 ratings)   Public Rating: 6.5 (2 ratings)

Predictable and Unpredictable in Quantum Mechanics by Ashkbiz Danehkar
5 posts  •  created by Ashkbiz Danehkar   •  Apr. 25, 2020 @ 14:59 GMT
Community Rating: 5.0 (3 ratings)   Public Rating: N/A

Impeccably Venerable: A Qualitative Conceptual Metaphysical Analysis of the Unknown by Dale Carl Gillman
15 posts  •  created by Dale Carl Gillman   •  Mar. 15, 2020 @ 00:34 GMT
Community Rating: 5.0 (3 ratings)   Public Rating: N/A

The Misalignment Problem by Jack James
10 posts  •  created by Jack James   •  Jan. 7, 2020 @ 17:54 GMT
Community Rating: 5.0 (6 ratings)   Public Rating: N/A

Indefinite causal structure can enhance predictability by Ding Jia
5 posts  •  created by Ding Jia   •  Apr. 25, 2020 @ 00:08 GMT
Community Rating: 5.0 (7 ratings)   Public Rating: N/A

'Undecidability', 'Uncomputability', and 'Unpredictability' are only the External features of Nature: An exploration with String-matter Universe Paradigm by Jayakar Johnson Joseph
3 posts  •  created by Jayakar Johnson Joseph   •  Apr. 23, 2020 @ 19:10 GMT
Community Rating: 5.0 (5 ratings)   Public Rating: N/A

Creative Undecidability of Real-World Dynamics and the Emergent Time Hierarchy by Andrei Kirilyuk
7 posts  •  created by Andrei Kirilyuk   •  Apr. 7, 2020 @ 12:51 GMT
Community Rating: 5.0 (2 ratings)   Public Rating: N/A

It takes a Decision to Decide if Decidability is True or False by Manfred U.E. Pohl
31 posts  •  created by Manfred U.E. Pohl   •  Jan. 14, 2020 @ 13:33 GMT
Community Rating: 5.0 (9 ratings)   Public Rating: 3.5 (2 ratings)

Complete Information Retrieval: A Fundamental Challenge by Chandrasekhar Roychoudhuri
8 posts  •  created by Chandrasekhar Roychoudhuri   •  Apr. 25, 2020 @ 17:37 GMT
Community Rating: 5.0 (6 ratings)   Public Rating: N/A

Mother of all Existence by Rajiv K Singh
6 posts  •  created by Rajiv K Singh   •  Feb. 25, 2020 @ 21:33 GMT
Community Rating: 5.0 (5 ratings)   Public Rating: 5.0 (2 ratings)

The Castle and elephants; Indescribable, undecidable, un-computable, and unpredictable by Georgina P. Woodward
68 posts  •  created by Georgina Woodward   •  Jan. 25, 2020 @ 12:48 GMT
Community Rating: 4.9 (9 ratings)   Public Rating: 8.5 (2 ratings)

Wisdom is to know by Madonna-Megara Morgana-Helena Holloway
19 posts  •  created by Madonna-Megara Morgana-Helena Holloway   •  Jan. 9, 2020 @ 22:03 GMT
Community Rating: 4.9 (8 ratings)   Public Rating: N/A

Unpredictability Implies an Abstract Reality by John Joseph Taylor
10 posts  •  created by John Joseph Taylor   •  Feb. 17, 2020 @ 21:48 GMT
Community Rating: 4.9 (8 ratings)   Public Rating: 5.5 (2 ratings)

Escaping Undecidability, Uncomputability, and Unpredictability with a new ‘Theory of Everything’ by David Jewson
14 posts  •  created by David Jewson   •  Mar. 31, 2020 @ 16:56 GMT
Community Rating: 4.8 (5 ratings)   Public Rating: N/A

Is the ether wind decidable? by John-Erik Persson
37 posts  •  created by John-Erik Persson   •  Feb. 6, 2020 @ 12:53 GMT
Community Rating: 4.8 (8 ratings)   Public Rating: 5.0 (1 rating)

What do undecidability and unpredictability mean? by Martin van Staveren
9 posts  •  created by Martin van Staveren   •  Mar. 20, 2020 @ 14:03 GMT
Community Rating: 4.8 (4 ratings)   Public Rating: N/A

The Primary Particle by Donald Alfred Sydney
7 posts  •  created by Donald Alfred Sydney   •  Jan. 22, 2020 @ 11:13 GMT
Community Rating: 4.8 (4 ratings)   Public Rating: N/A

An extended Rice's Theorem and some of its conhsequences by Francisco Antonio Doria
11 posts  •  created by Francisco Antonio Doria   •  Feb. 10, 2020 @ 12:39 GMT
Community Rating: 4.7 (6 ratings)   Public Rating: N/A

Pushing the envelope: cosmology and the limits of knowledge by Kyle Miller
2 posts  •  created by Kyle Miller   •  Apr. 24, 2020 @ 22:40 GMT
Community Rating: 4.7 (3 ratings)   Public Rating: N/A

Unbaked Layer Cake by Ernesto Vaca
22 posts  •  created by Ernesto Vaca   •  Apr. 9, 2020 @ 18:33 GMT
Community Rating: 4.7 (6 ratings)   Public Rating: 4.0 (1 rating)

A Matter of Time by Arto Annila
6 posts  •  created by Arto Annila   •  Apr. 23, 2020 @ 15:46 GMT
Community Rating: 4.5 (4 ratings)   Public Rating: N/A

Consciousness as Foundation of the Physical World by Dr Narayan Kumar Bhadra
11 posts  •  created by Dr Narayan Kumar Bhadra   •  Mar. 11, 2020 @ 01:23 GMT
Community Rating: 4.5 (8 ratings)   Public Rating: 8.5 (27 ratings)

From uncomputability to quantum consciousness to quantum gravity to neutrinos masses measurement by Janko Kokosar
8 posts  •  created by Janko Kokosar   •  Mar. 9, 2020 @ 22:45 GMT
Community Rating: 4.5 (4 ratings)   Public Rating: N/A

Evaluate, Rehabilitate, Correct, and Decrease - Undecidability, Uncomputability, and Unpredictability by Gilbert Leon Beaudry
7 posts  •  created by Gilbert Leon Beaudry   •  Apr. 20, 2020 @ 10:35 GMT
Community Rating: 4.4 (5 ratings)   Public Rating: N/A

On creating thr world by Jeffrey Nicholls
4 posts  •  created by Jeffrey Nicholls   •  Apr. 25, 2020 @ 01:32 GMT
Community Rating: 4.4 (5 ratings)   Public Rating: N/A

Tessellation and concentration in quantized space by Sydney Ernest Grimm
35 posts  •  created by S.E. Grimm   •  Feb. 23, 2020 @ 17:37 GMT
Community Rating: 4.4 (8 ratings)   Public Rating: N/A

No mathematics without mathematicians, no physics without physicists by Per Östborn
6 posts  •  created by Per Östborn   •  Mar. 20, 2020 @ 14:05 GMT
Community Rating: 4.3 (3 ratings)   Public Rating: N/A

We are made of math by Luis F Patino
9 posts  •  created by Luis F Patino   •  Apr. 25, 2020 @ 17:34 GMT
Community Rating: 4.3 (6 ratings)   Public Rating: N/A

Uncomputability, Intractability and the Multiverse by Ruben Ruiz-Torrubiano
5 posts  •  created by Ruben Ruiz-Torrubiano   •  Apr. 13, 2020 @ 11:47 GMT
Community Rating: 4.3 (3 ratings)   Public Rating: N/A

Thermal Approximations: Probability, Energy, and the Unknowable by Scott W Schwartz
2 posts  •  created by Scott W Schwartz   •  Apr. 20, 2020 @ 13:58 GMT
Community Rating: 4.3 (3 ratings)   Public Rating: N/A

Are Qualia Computable? Godel, Infinite Regress and Distributional Semantics by Xerxes D. Arsiwalla
4 posts  •  created by Xerxes Arsiwalla   •  Apr. 25, 2020 @ 11:56 GMT
Community Rating: 4.3 (4 ratings)   Public Rating: N/A

Undecidability, Uncomputability, and Unpredictability is not Consistent with the Scientific Method by Scott S Gordon
20 posts  •  created by Scott S Gordon   •  Feb. 5, 2020 @ 15:57 GMT
Community Rating: 4.3 (8 ratings)   Public Rating: N/A

The Flip by Simon Burton
7 posts  •  created by Simon Burton   •  Apr. 25, 2020 @ 00:33 GMT
Community Rating: 4.2 (5 ratings)   Public Rating: 9.5 (2 ratings)

TOWARD A GENERAL THEORY OF REALITY by Agus H Budiyanto
9 posts  •  created by Agus H Budiyanto   •  Apr. 25, 2020 @ 01:41 GMT
Community Rating: 4.1 (7 ratings)   Public Rating: N/A

How to Solve Moral Conundrums with Computability Theory by Jonogmin Baek
13 posts  •  created by Jongmin Baek   •  Apr. 21, 2020 @ 11:09 GMT
Community Rating: 4.0 (3 ratings)   Public Rating: N/A

NON-COMPUTABILITY AND UNPREDICTABILITY ARE SO YESTERDAY: WITH COMPUTABLE AND PREDICTABLE COSMIC STRUCTURE, PLUS IMPLICATIONS FOR MATHEMATICS AND SCIENCE by Rodney Bartlett
36 posts  •  created by Rodney Bartlett   •  Feb. 2, 2020 @ 12:09 GMT
Community Rating: 4.0 (5 ratings)   Public Rating: N/A

Mind-forg’d Manacles and Somewhat Free Will by Steven R Brock
2 posts  •  created by Steven R Brock   •  Apr. 25, 2020 @ 14:59 GMT
Community Rating: 4.0 (2 ratings)   Public Rating: N/A

The Ultimate decidability, computability, and predictability of all things and processes. by Paul N Butler
33 posts  •  created by Paul N Butler   •  Mar. 15, 2020 @ 22:37 GMT
Community Rating: 4.0 (3 ratings)   Public Rating: N/A

Is the Theory of Everything Lurking in Uncomputability? by Irek Defee
9 posts  •  created by Irek Defee   •  Apr. 23, 2020 @ 12:12 GMT
Community Rating: 4.0 (5 ratings)   Public Rating: N/A

Malus Law with local hidden variables, and a backwards-in-time solution for Bell’s Theorem by austin james fearnley
6 posts  •  created by austin fearnley   •  Apr. 23, 2020 @ 12:11 GMT
Community Rating: 4.0 (4 ratings)   Public Rating: N/A

Undecidability as the Framework for Quantum Theory and Spacetime by Baruch Garcia
2 posts  •  created by Baruch Garcia   •  Apr. 23, 2020 @ 22:22 GMT
Community Rating: 4.0 (4 ratings)   Public Rating: N/A

Evolving Unpredictability by Thiago Guerreiro
3 posts  •  created by Thiago Guerreiro   •  Apr. 22, 2020 @ 20:22 GMT
Community Rating: 4.0 (2 ratings)   Public Rating: 9.2 (10 ratings)

LIMITS OF “LIMIT”. INCOMPLETENESS, UNDECIDABILITY & NON-COMPUTABLE VALUES: IMPLICATIONS IN QUANTUM PHYSICS by basudeba mishra
7 posts  •  created by basudeba mishra   •  Mar. 12, 2020 @ 14:49 GMT
Community Rating: 4.0 (3 ratings)   Public Rating: N/A

Free Will by Grace M Lo Porto
17 posts  •  created by Grace M Lo Porto   •  Jan. 27, 2020 @ 18:35 GMT
Community Rating: 3.9 (7 ratings)   Public Rating: 2.0 (1 rating)

Substrate-targeted programming by Philip Thrift
10 posts  •  created by Philip Thrift   •  Apr. 24, 2020 @ 23:40 GMT
Community Rating: 3.9 (7 ratings)   Public Rating: 7.0 (1 rating)

Determinism must strike back by Edward Levi
4 posts  •  created by Edward Levi   •  Apr. 3, 2020 @ 14:41 GMT
Community Rating: 3.8 (5 ratings)   Public Rating: N/A

WHY CAN’T Y’ALL SEE THING MY WAY? by Joe Fisher
15 posts  •  created by Joe William Fisher   •  Jan. 7, 2020 @ 17:54 GMT
Community Rating: 3.7 (10 ratings)   Public Rating: 3.7 (3 ratings)

Undecidability, Uncomputability and Unpredictability the three pillars of Anti-realism by Jose P. Koshy
6 posts  •  created by Jose P. Koshy   •  Feb. 25, 2020 @ 11:24 GMT
Community Rating: 3.7 (3 ratings)   Public Rating: 4.5 (2 ratings)

A Redefinition of the Notion of Truth by Paul McKarris
6 posts  •  created by Paul McKarris   •  Apr. 23, 2020 @ 17:35 GMT
Community Rating: 3.7 (3 ratings)   Public Rating: 7.7 (3 ratings)

There is a Simple Reason Physics and Science have reached what appears to be a limit and cannot at present get over it and move forward with the certainty of the Physics of Galileo and Newton in their time. by Gerry Leslie Klein
4 posts  •  created by Gerry Leslie Klein   •  Apr. 25, 2020 @ 15:07 GMT
Community Rating: 3.6 (5 ratings)   Public Rating: 7.0 (1 rating)

The illusion of structure or insufficiency of approach? the un(3) of unruly problems by Bradly John Alicea
2 posts  •  created by Bradly John Alicea   •  Mar. 20, 2020 @ 14:05 GMT
Community Rating: 3.5 (2 ratings)   Public Rating: N/A

On the computability of the cosmic matter density from first principles by Shawn Halayka
44 posts  •  created by Shawn Halayka   •  Mar. 9, 2020 @ 22:45 GMT
Community Rating: 3.5 (6 ratings)   Public Rating: N/A

To find the origin of these no go areas, quantum mechanics is the main question, as the rest is often limitations of the mathematical description. For the deep randomness in QM, missing concepts must be found, as in a new interpretation published in 2019.
7 posts  •  created by Jonathan Kerr   •  Apr. 6, 2020 @ 14:59 GMT
Community Rating: 3.5 (4 ratings)   Public Rating: 8.5 (2 ratings)

A Functional Guide to Information, Intelligence, and Agency by Edward Kneller
1 post  •  created by Edward Kneller   •  Apr. 24, 2020 @ 20:33 GMT
Community Rating: 3.5 (4 ratings)   Public Rating: N/A

The Sun Clearly Goes Around the Earth by Al Schneider
13 posts  •  created by Al Schneider   •  Feb. 17, 2020 @ 19:32 GMT
Community Rating: 3.5 (6 ratings)   Public Rating: N/A

Black Hole Zero-Knowledge Proofs by Melanie Swan
2 posts  •  created by Melanie Swan   •  Mar. 12, 2020 @ 22:50 GMT
Community Rating: 3.5 (2 ratings)   Public Rating: N/A

The Calculational Scientist: But does Nature calculate anything at all ? by Joachim J. Wlodarz
5 posts  •  created by Joachim J. Wlodarz   •  Apr. 24, 2020 @ 22:41 GMT
Community Rating: 3.4 (9 ratings)   Public Rating: N/A

CAN THE FUTURE CREATE THE PAST? by Gyöngyi Bokor
8 posts  •  created by Gyongyi Bokor   •  Apr. 25, 2020 @ 12:16 GMT
Community Rating: 3.4 (7 ratings)   Public Rating: N/A

Phy vs Psy. Sic or chic? by Joseph Maria Hoebe
12 posts  •  created by Joseph Maria Hoebe   •  Jan. 27, 2020 @ 18:34 GMT
Community Rating: 3.4 (5 ratings)   Public Rating: 6.6 (9 ratings)

No knowing Time definition and experimental meaning, Force physicists to theories creation, that make Physics Undecidable, Incomputable and Unpredictable. by Héctor Daniel Gianni
6 posts  •  created by Héctor Daniel Gianni   •  Apr. 5, 2020 @ 23:03 GMT
Community Rating: 3.3 (3 ratings)   Public Rating: N/A

Natural Unity by James A Putnam
6 posts  •  created by James A Putnam   •  Apr. 25, 2020 @ 01:32 GMT
Community Rating: 3.3 (6 ratings)   Public Rating: N/A

Fundamentals that Ensure Undecidability, Uncomputability, and Unpredictability by C. Sperry Andrews 4th
7 posts  •  created by Charles Sperry Andrews IV   •  Mar. 4, 2020 @ 02:37 GMT
Community Rating: 3.3 (4 ratings)   Public Rating: N/A

Predictability is pointless by Michael Papp
4 posts  •  created by Michael Papp   •  Apr. 23, 2020 @ 22:24 GMT
Community Rating: 3.3 (4 ratings)   Public Rating: N/A

ON THE ORIGIN AND EVOLUTION OF CONSCIOUSNESS by sherman loran jenkins
6 posts  •  created by sherman loran jenkins   •  Apr. 24, 2020 @ 13:33 GMT
Community Rating: 3.2 (5 ratings)   Public Rating: 10.0 (2 ratings)

Reality is a simple mathematical structure literally, hence computable by Adel Hassan Sadeq
5 posts  •  created by adel sadeq   •  Apr. 25, 2020 @ 17:39 GMT
Community Rating: 3.2 (6 ratings)   Public Rating: N/A

Relieving Tensions in Modern Physics and Astronomy. by DURGA DAS DATTA.
6 posts  •  created by DURGA DAS DATTA.   •  Jan. 8, 2020 @ 19:30 GMT
Community Rating: 3.1 (8 ratings)   Public Rating: N/A

Viewing paradox through the lens of general relativity. by Chris Blackwood
8 posts  •  created by Chris Blackwood   •  Apr. 21, 2020 @ 11:14 GMT
Community Rating: 3.0 (3 ratings)   Public Rating: N/A

Knowledge is power by PRASAD RAMESH DIVATE
9 posts  •  created by PRASAD RAMESH DIVATE   •  Apr. 15, 2020 @ 13:14 GMT
Community Rating: 3.0 (3 ratings)   Public Rating: N/A

Quantum strangeness from the uncomputability of nature by Tung Ten Yong
7 posts  •  created by Tung Ten Yong   •  May. 6, 2020 @ 20:10 GMT
Community Rating: 2.8 (6 ratings)   Public Rating: N/A

Common 3D Physics Depicts Universe Emerging From Chaos by Charles John Sven
6 posts  •  created by Charles John Sven   •  Jan. 18, 2020 @ 12:46 GMT
Community Rating: 2.8 (5 ratings)   Public Rating: 6.9 (9 ratings)

Life, the Universe and Time: Who Would Want to Live in a Predictable Universe Anyway? by C.C. Walters
7 posts  •  created by nancy walters   •  Apr. 25, 2020 @ 17:47 GMT
Community Rating: 2.8 (8 ratings)   Public Rating: N/A

From inability to facility by James Robert Arnold
7 posts  •  created by James Arnold   •  May. 9, 2020 @ 14:32 GMT
Community Rating: 2.7 (6 ratings)   Public Rating: N/A

The Infinite Void As The Paradoxical Origin of The Universe by Michael Hugh Falconar
2 posts  •  created by Michael Hugh Falconar   •  Apr. 25, 2020 @ 15:05 GMT
Community Rating: 2.7 (3 ratings)   Public Rating: N/A

The Un-decidable as Natural Unit of physical Information: “Mind” as the Quantum Vacuum, “Matter” as its Interference Pattern by Chidi Idika
2 posts  •  created by Chidi Idika   •  Apr. 24, 2020 @ 21:10 GMT
Community Rating: 2.7 (3 ratings)   Public Rating: N/A

A Musinf upon the Nature of Fundamental Objects vis-a-vis the Point and the Plane by Vinay Seth
8 posts  •  created by Vinay Seth   •  Apr. 25, 2020 @ 17:40 GMT
Community Rating: 2.6 (5 ratings)   Public Rating: N/A

Fundamental time and relativity by Gene H Barbee
5 posts  •  created by Gene H Barbee   •  Mar. 20, 2020 @ 17:59 GMT
Community Rating: 2.5 (4 ratings)   Public Rating: N/A

Mathematics and the demarcation problem by Wim Christiaens
2 posts  •  created by Wim Christiaens   •  Apr. 23, 2020 @ 13:11 GMT
Community Rating: 2.5 (4 ratings)   Public Rating: N/A

The meaning of predicting yourself and the limits of objetivation by juan manuel jones volonte
3 posts  •  created by juan manuel jones volonte   •  Apr. 24, 2020 @ 22:43 GMT
Community Rating: 2.5 (4 ratings)   Public Rating: N/A

Unpredictability of Quantum Particles and Effect of Gravity by Amrit Ladhani
8 posts  •  created by Amrit Ladhani   •  Feb. 21, 2020 @ 16:44 GMT
Community Rating: 2.5 (4 ratings)   Public Rating: N/A

Primarily True by Michael Smith
9 posts  •  created by Michael Smith   •  Mar. 1, 2020 @ 12:58 GMT
Community Rating: 2.5 (4 ratings)   Public Rating: N/A

counting quantum information in our universe by Paul F. OBrien
5 posts  •  created by Paul OBrien OBrien   •  Apr. 25, 2020 @ 17:32 GMT
Community Rating: 2.4 (5 ratings)   Public Rating: N/A

THE PATTERN OF CRACKS IS UNPREDICTABLE, BUT NOT TO CRACK IS DECIDABLE by michael kowalczyk
3 posts  •  created by michael kowalczyk   •  Mar. 24, 2020 @ 15:40 GMT
Community Rating: 2.3 (4 ratings)   Public Rating: 6.8 (6 ratings)

Twisting the limits by Thad Roberts
1 post  •  created by Thad Roberts   •  Apr. 24, 2020 @ 21:50 GMT
Community Rating: 2.3 (4 ratings)   Public Rating: N/A

Predicting Velocities of Stars by Michael Dalton
8 posts  •  created by Michael Dalton   •  Apr. 17, 2020 @ 21:47 GMT
Community Rating: 2.0 (3 ratings)   Public Rating: N/A

Indeterminacy generated by space-time by Jiří Šrajer
6 posts  •  created by Jiří Šrajer   •  Apr. 3, 2020 @ 01:22 GMT
Community Rating: 2.0 (2 ratings)   Public Rating: 8.5 (2 ratings)

Interaction of the self with all else by Bala R Subramanian
4 posts  •  created by Bala R Subramanian   •  Mar. 22, 2020 @ 01:36 GMT
Community Rating: 2.0 (3 ratings)   Public Rating: 5.5 (2 ratings)

Impressions of decidability computability and predictability - inexpert eccentric take. by marcovici cristian alexandru
5 posts  •  created by marcovici cristian alexandru   •  Apr. 22, 2020 @ 20:23 GMT
Community Rating: 1.8 (5 ratings)   Public Rating: 7.0 (1 rating)

Prioritizing non-fiction amounts to unbelievability by Daniel Thomas Hawkley
5 posts  •  created by Daniel Thomas Hawkley   •  Apr. 7, 2020 @ 18:43 GMT
Community Rating: 1.7 (3 ratings)   Public Rating: N/A

Undecidability, Uncomputability, and Unpredictability or how Science has run into the Q-problem by Dmitri Martila
4 posts  •  created by Dmitri Martila   •  Mar. 22, 2020 @ 01:35 GMT
Community Rating: 1.7 (3 ratings)   Public Rating: 5.5 (2 ratings)

Quantum mechanics and the flow of time by carl sebastian andersson
8 posts  •  created by carl sebastian   •  Apr. 22, 2020 @ 20:19 GMT
Community Rating: 1.6 (5 ratings)   Public Rating: N/A

The Discernible Universe? Absolutely by vito robert D'Angelo
4 posts  •  created by vito robert D'Angelo   •  Apr. 7, 2020 @ 12:53 GMT
Community Rating: 1.3 (3 ratings)   Public Rating: N/A
"""

re.findall('Community Rating\: [\d\.]+ \(\d\d ratings?\)', text)