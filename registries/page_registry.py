from src.pages.main_menu import MainMenu
from src.pages.statistics import *
from src.pages.calculus import *
from src.pages.linearalgebra import *
from src.pages.advalgebra import *

PAGE_REGISTRY = [
    MainMenu,

    # --- STATISTICS PAGES ---
    StatsPage,
    DescStatsPage,
    ProbDistPage,
    HypothesisPage,
    AnovaPage,
    RegressionPage,
    BayesianPage,

    # --- CALCULUS PAGES ---
    CalcPage,
    DerivPage,
    IntegrationPage,
    LimitsPage,
    DiffPage,
    TaylorMacPage,

    # --- LINEAR ALGEBRA PAGES ---
    LinAlgPage,
    MatrixOpPage,
    DeterInverPage,
    EigenCalcPage,
    SysOfEqPage,
    VectAnalPage,

    # --- ADVANCED ALGEBRA PAGES ---
    AdvAlgPage,
    PolySolvPage,
    LogExpPage,
    PartFracDecPage,
    CompNumbPage
]