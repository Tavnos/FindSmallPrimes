class class_find_factor:
    find_factor_list = []
    primes_list = []
    def find_factor_of(self, the_integer):
        self.find_factor_list = []
        for i in range(the_integer):
            if (the_integer / (i+1)) == int(the_integer /(i+1)):
                if (i+1 != 1) and (i+1 != the_integer):
                    self.find_factor_list += [i+1]
    def find_primes_upto(self, search_range):
        self.primes_list = []
        for i in range(search_range):
            self.find_factor_of(i)
            if len(self.find_factor_list) > 0:
                pass
            elif i != 0 and i != 1:
                self.primes_list += [i]
init_find_factor = class_find_factor()
init_find_factor.find_primes_upto(10000)
print(init_find_factor.primes_list)