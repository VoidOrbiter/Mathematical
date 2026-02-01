from src.pages.main_menu import MainMenu
from src.pages.statistics import *
from src.pages.calculus import *
from src.pages.linearalgebra import *
from src.pages.advalgebra import *

PAGE_MANIFEST = [

    # --- MAIN MENU PAGES OWNED BY MAIN MENU ---
    {"page": MainMenu, "name": "MainMenu", "owner": "Window"},
    {"page": StatsPage, "name": "Statistics", "owner": "MainMenu"},
    {"page": CalcPage, "name": "Calculus", "owner": "MainMenu"},
    {"page": LinAlgPage, "name": "Linear Algebra", "owner": "MainMenu"},
    {"page": AdvAlgPage, "name": "Advanced Algebra", "owner": "MainMenu"},

    # --- STATISTIC PAGES OWNED BY STATS PAGE ---
    {"page": DescStatsPage, "name": "Descriptive Stats", "owner": "StatsPage"},
    {"page": ProbDistPage, "name": "Probability Distributions", "owner": "StatsPage"},
    {"page": HypothesisPage, "name": "Hypothesis Testing", "owner": "StatsPage"},
    {"page": AnovaPage, "name": "ANOVA (Group Comparison)", "owner": "StatsPage"},
    {"page": RegressionPage, "name": "Linear Regression", "owner": "StatsPage"},
    {"page": BayesianPage, "name": "Bayesian Inference", "owner": "StatsPage"},

    # ----- CALCULUS PAGES OWNED BY CALC PAGE ---
    {"page": DerivPage, "name": "Derivatives", "owner": "CalcPage"},
    {"page": IntegrationPage, "name": "Integration", "owner": "CalcPage"},
    {"page": LimitsPage, "name": "Limits && Continuity", "owner": "CalcPage"},
    {"page": DiffPage, "name": "Differential Equations", "owner": "CalcPage"},
    {"page": TaylorMacPage, "name": "Taylor/Maclaurin Series", "owner": "CalcPage"},

    # ---- LINEAR ALGEBRA OWNED BY LINALG PAGE
    {"page": MatrixOpPage, "name": "Matrix Operations", "owner": "LinAlgPage"},
    {"page": DeterInverPage, "name": "Determinants && Inverses", "owner": "LinAlgPage"},
    {"page": EigenCalcPage, "name": "Eigen-Calculations", "owner": "LinAlgPage"},
    {"page": SysOfEqPage, "name": "System of Equations", "owner": "LinAlgPage"},
    {"page": VectAnalPage, "name": "Vector Analysis", "owner": "LinAlgPage"},

    # --- ADVANCED ALGEBRA OWNED BY ADVALG PAGE ---
    {"page": PolySolvPage, "name": "Polynomial Solver", "owner": "AdvAlgPage"},
    {"page": LogExpPage, "name": "Logarithms && Exponents", "owner": "AdvAlgPage"},
    {"page": PartFracDecPage, "name": "Partial Fraction Decomposition", "owner": "AdvAlgPage"},
    {"page": CompNumbPage, "name": "Complex Numbers", "owner": "AdvAlgPage"}
]