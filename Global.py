calls = 0
def count_calls():
    global calls
    calls = calls + 1              ### Или calls += 1
def string_info(string):
    count_calls()
    stringr = str(string)
    result = (len(stringr), stringr.upper(), stringr.lower())
    return result
def is_contains(string, list_to_search):
    count_calls()
    stringr = str(string).upper()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).upper() == stringr:
            result = True
            break
        else:
            result = False
            continue
    return result
print(string_info('MosCow3424'))
print(string_info('GloBalsds22dsd'))
print(is_contains('moscow', ['mosCOW', 'BUda', 'paris']))
print(is_contains('FIrE', ['WATER', 'Fire', 'sTone', 'eArth']))
print(is_contains('sdsdsd', ['SDSDsd2', 'dsdsds', 'rerere', 'RerRe']))
print(calls)
print(string_info('MosCow342422'))
print(calls)
