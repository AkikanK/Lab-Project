import unittest
from algorithmv3 import Mark3_nodepth1
class Testing(unittest.TestCase):

    def setUp(self):
        return super().setUp()
    
    def test_hello_world(self):
        self.assertEqual("Hello World", "Hello World")

    def test_acceptable_values(self):
        M = Mark3_nodepth1()  

        tests = [
            (0, 0),  # Valid
            (1, 1),  # Valid
            (2, 2),  # Valid
        ]

        for value in tests:
            M.current = value[0]
            self.assertEqual(M.current, value[1])
    
    def test_not_a_number(self):
        M = Mark3_nodepth1()

        with self.assertRaises(ValueError) as context:
            M.current = "Rock"

        self.assertEqual(str(context.exception), "Value must be an integer.")

    def test_not_in_range(self):
        M = Mark3_nodepth1()

        tests = [-1, 3, -20, 30]
        for value in tests:
            with self.assertRaises(ValueError) as context:
                M.current = value

            self.assertEqual(str(context.exception), "Value must be in the range [0, 2].")
    
    def test_push_too_long(self):
        M = Mark3_nodepth1()
        M.past_plays = [0,0,0,0,0,0]

        M.push(1)
        self.assertEqual(M.past_plays, [0,0,0,0,0,1])

    def test_breaking_the_test_function(self): #Overall tests the Rock-Paper-Scissors game itself as well
        M = Mark3_nodepth1()
        M.past_plays = [0,2,1,2,2]
        self.assertIsNone(M.test(1,3)) #Testing to see if you can place a value outside of range in RPS

    def test_proper_past_prob(self): #Checks that past probabilities are stored properly
        M = Mark3_nodepth1()
        M.past_plays = [0,2,1,1]
        M.past_propb()

        #Check that something is stored:
        self.assertIsNotNone(M.fours)
        self.assertIsNotNone(M.triples)

        #Check each dictionary for proper storage:
        self.assertEqual(M.triples, {(2,1,1): 1})
        self.assertEqual(M.fours, {(0,2,1,1): 1})
        self.assertEqual(M.fives, {})

    def test_get_some_value(self):
        M = Mark3_nodepth1()
        self.assertIsNotNone(M.current_propb())

    #THESE FOLLOWING TESTS CHECK THE CORE LOGIC OF THE ALGORITHM
    #THEY ALSO CHECK THAT ASSESS WORKS PROPERLY FOR ALL LEVELS,
    #BUT I WILL ALSO CARRY OUT MORE TESTS ON THE ASSESS FUNCTION BELOW

    def test_switching_of_level(self):
        M = Mark3_nodepth1()
        M.past_plays = [0,0,0,0,0,0]
        M.past_propb()
        for key in M.data:
            M.data[key] = 10
            self.assertIsNotNone(M.current_propb())
            self.assertEqual(M.current_propb(), 1) #tests that each level succeeds -- SEE THE NEXT TEST
            M.data[key] = 0

    def test_sanity(self): #IMPORTANT TEST
        M = Mark3_nodepth1()
        M.past_plays = [0,0,0,0,0,0]
        M.past_propb()
        for key in M.data:
            M.data[key] = 10
            self.assertEqual(M.current_propb(), 1) #TESTS IF EACH LEVEL CAN REACT TO BASIC SPAM
            M.data[key] = 0

    def test_empty_past_plays(self): #Checks empty play handling
        M = Mark3_nodepth1()
        M.past_plays = []
        M.past_propb()
        self.assertEqual(M.triples, {})
        self.assertEqual(M.fours, {})
        self.assertEqual(M.fives, {})
        self.assertIsNone(M.assess(2, M.past_plays, M.triples))

    def test_large_past_plays(self): #does the past play handle very long sets?
        M = Mark3_nodepth1()
        M.past_plays = [0, 1, 2] * 1000
        M.past_propb()
        self.assertGreater(len(M.triples), 0)

    #ALL OF THESE TESTS ARE TO PROVE THAT THE ASSESS FUNCTION WORKS AS INTENDED

    def test_assess_output_validity(self): #Invariance test // Check that the assess function works consistently
        M = Mark3_nodepth1()
        M.past_plays = [0, 1, 2, 0, 1, 2]
        M.past_propb()
        result = M.assess(2, M.past_plays, M.triples)
        self.assertIn(result, [0, 1, 2, None])

    def test_complete_nonsense_assess(self):
        M = Mark3_nodepth1()
        M.past_plays = [0,1,1,0,1]
        M.past_propb() #Primes the assess to actually function when needed

        with self.assertRaises(TypeError):
            M.assess(0, 0, 0)
            M.assess("Four", M.past_plays, M.triples) #String should raise error
            M.assess(2, [2,0,3,0,2,2,1,3,4,2,], M.triples) #Trying to inject a random string
            M.assess(2, M.past_plays, M.sixes) #last dictionary doesn't match depth --> Results in listindexoutofrange

    def test_nothing_to_assess(self):
        M = Mark3_nodepth1()
        M.past_plays = [1,0,1,0,1]
        M.triples = {
        (0, 1, 0): 2,
        (1, 0, 1): 1
        } #Here I will inject a value for triples, and see that it returns the right value
        M.past_propb() #Primes the assess to actually function when needed
        self.assertIsNone(M.assess(5, M.past_plays, M.sixes)) #tests that with this priming the other dictionaries are not affected
        self.assertIsNotNone(M.assess(2, M.past_plays, M.triples))

        self.assertEqual(M.assess(2, M.past_plays, M.triples), 1) #should make the prediction that it should play a Paper (player most likely to choose Rock)

    #LASTLY IS TO TEST THE ENTIRE BULK TOGETHER:

    def test_integration(self): #Integration of all the functions (Done in other parts, but also here separately)
        M = Mark3_nodepth1()
        M.past_plays = [0, 1]
        M.past_propb()
        M.push(2)  # Push a new move
        M.past_propb()
        M.push(0)  # Push a new move
        M.past_propb()
        M.push(1)  # Push a new move
        M.past_propb()
        M.push(2)  # Push a new move
        M.past_propb()
        print(M.past_plays)
        M.past_propb()
        result = M.assess(2, M.past_plays, M.triples)
        self.assertIn(result, [0, 1, 2])
    
    def test_end_to_end(self): #Testing if player moves are countered properly (Almost same as before, but with 'fake-user-input')
        M = Mark3_nodepth1()
        M.past_plays = [0, 1]
        M.past_propb()
        M.push(2)  # Push a new move
        M.past_propb()
        M.push(0)  # Push a new move
        M.past_propb()
        M.push(1)  # Push a new move
        M.past_propb()
        M.push(2)  # Push a new move
        M.past_propb()
        rounds = [(0, 2), (1, 0), (2, 1)]  # Player choices and theri expected computer responses!
        for player_move, expected_comp_move in rounds:
            M.push(player_move)
            M.past_propb()
            result = M.assess(2, M.past_plays, M.triples)
            self.assertEqual(result, expected_comp_move)

    def test_performance(self):
        import time
        M = Mark3_nodepth1()
        M.past_plays = [0, 1, 2] * 10000  # Large dataset
        start_time = time.time()
        M.past_propb()
        end_time = time.time()
        self.assertLess(end_time - start_time, 1.0)  #I am still ensuring it runs in under 1 second, which based on past tests it should