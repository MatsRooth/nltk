# Natural Language Toolkit: Combinatory Categorial Grammar
#
# Copyright (C) 2001-2020 NLTK Project
# Author: Tanin Na Nakorn (@tanin)
# New version of compute_type_raised_semantics: Mats Rooth
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT
"""
Helper functions for CCG semantics computation
"""

from nltk.sem.logic import *


def compute_type_raised_semantics(semantics):
    varf = Variable('F')
    vara = Variable('z')
    expf = FunctionVariableExpression(varf)
    expa = FunctionVariableExpression(vara)

    raiser = LambdaExpression(vara,LambdaExpression(varf,ApplicationExpression(expf, expa)))

    semantics2 = ApplicationExpression(raiser,semantics)
    return semantics2.simplify()


def compute_function_semantics(function, argument):
    return ApplicationExpression(function, argument).simplify()


def compute_composition_semantics(function, argument):
    assert isinstance(argument, LambdaExpression), (
        "`" + str(argument) + "` must be a lambda expression"
    )
    return LambdaExpression(
        argument.variable, ApplicationExpression(function, argument.term).simplify()
    )


def compute_substitution_semantics(function, argument):
    assert isinstance(function, LambdaExpression) and isinstance(
        function.term, LambdaExpression
    ), ("`" + str(function) + "` must be a lambda expression with 2 arguments")
    assert isinstance(argument, LambdaExpression), (
        "`" + str(argument) + "` must be a lambda expression"
    )

    new_argument = ApplicationExpression(
        argument, VariableExpression(function.variable)
    ).simplify()
    new_term = ApplicationExpression(function.term, new_argument).simplify()

    return LambdaExpression(function.variable, new_term)
