from nltk.ccg import chart, lexicon
from nltk.ccg.chart import printCCGDerivation


print('''==============================
===       Lexicon l3       ===
==============================
''')
l3 = lexicon.fromstring('''
:- S, NP
Justin => NP {\P.P(j)}
Keisha => NP {\P.P(k)}
somebody => NP {\P.exists x.(person(x) & P(x))}
everybody => NP {\P.forall x.(person(x) -> P(x))}
admires => (S\\NP)/NP {\Y.(\Z.Z(\z.Y(\y.admire(z,y))))}
complains => S\\NP {complain}
''', True)

print(l3)
print()


print('''====================================================================================
=== Derivation for \'somebody admires everybody\' obtained with ApplicationRuleSet ===
=== The semantics is the expected one.                                           ===
====================================================================================''')



parser1 = chart.CCGChartParser(l3, chart.ApplicationRuleSet)
parses = list(parser1.parse("somebody admires everybody".split()))
printCCGDerivation(parses[0])


print('''
=======================================================================================
=== Derivation for \'somebody admires everybody\' obtained with                       ===
=== ForwardTypeRaiseRule + ForwardApplication.                                      ===
=== The result has scrambled scopes when run in the development branch.             ===
=======================================================================================''')

RightwardRuleSet = [chart.BinaryCombinatorRule(chart.ForwardApplication),chart.ForwardTypeRaiseRule()]

parser2 = chart.CCGChartParser(l3, RightwardRuleSet)
parses = list(parser2.parse("somebody admires everybody".split()))
printCCGDerivation(parses[0])

print('''
=======================================================================================
=== Derivation for \'Justin admires Justin\' obtained with                            ===
=== ForwardTypeRaiseRule + ForwardApplication. When run in the development branch,  ===
=== the result is ill-formed, and a free F appears.                                 ===
=======================================================================================''')

parses = list(parser2.parse("Justin admires Justin".split()))
printCCGDerivation(parses[0])
