t_val =0 
        for i in range(len(s)):
            if i > o and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] -2 * rom_val[s[i - 2]]
            else:
                int_val += rom_val[s[i]]
            return int_val
print(py_solution().roman_to_int('MMMCMLXXXVI'))
print(py_solution().roman_to_int('MMMM'))
print(py_solution().roman_to_int('c'))
