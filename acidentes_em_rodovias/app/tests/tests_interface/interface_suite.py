from tests_acidentes_rodovias_periodo import *
from tests_acidentes_rodovias_regiao import *

def suite_tests_interface():
    suite1 = unittest.TestLoader().loadTestsFromTestCase(AcidentesRodoviasRegiaoTestCase)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(AcidentesRodoviasPeriodoTestCase)
    alltests = unittest.TestSuite([suite1, suite2])

    return alltests

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite_tests_interface()
    runner.run(test_suite)
