from memes import meme_db
from match import match
from typing import List, Tuple, Callable, Any
def get_name(meme: Tuple[str,int,int,str]) -> str:
    return meme[0]


def get_year(meme: Tuple[str,int,int,str]) -> int:
    return meme[1]


def get_rank(meme: Tuple[str,int,int,str]) -> int:
    return meme[2]


def get_desc(meme: Tuple[str,int,int,str]) -> str:
    return meme[3]



def year_by_name(matches: List[str]) -> List[int]:
    result:List[int]=[]
    for i in meme_db:
        if get_name(i)==matches[0]:
            result.append(int(get_year(i)))
    return result

def name_by_year(matches: List[str]) -> List[str]:
    result:List[str]=[]
    for i in meme_db:
        if get_year(i)==int(matches[0]):
            result.append(get_name(i))
    return result


def name_by_year_range(matches: List[str]) -> List[str]:
    result:List[str]=[]
    for i in meme_db:
        if get_year(i)>=int(matches[0]) and get_year(i)<=int(matches[1]):
                result.append(get_name(i))
    return result


def name_before_year(matches: List[str]) -> List[str]:
    result:List[str]=[]
    for i in meme_db:
        if get_year(i)<int(matches[0]):
            result.append(get_name(i))
    return result


def name_after_year(matches: List[str]) -> List[str]:
    result:List[str]=[]
    for i in meme_db:
        if get_year(i)>int(matches[0]):
            result.append(get_name(i))
    return result

def desc_by_name(matches: List[str]) -> List[int]:
    result:List[int]=[]
    for i in meme_db:
        if get_name(i)==matches[0]:
            result.append(int(get_desc(i)))
    return result

def rank_by_name(matches: List[str]) -> List[int]:
    result:List[int]=[]
    for i in meme_db:
        if get_name(i)==matches[0]:
            result.append(int(get_rank(i)))
    return result


def bye_action(dummy: List[str]) -> None:
    raise KeyboardInterrupt


pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("when was % popular"), year_by_name),
    (str.split("what was popular in _"), name_by_year),
    (str.split("what was popular between _ and _"), name_by_year_range),
    (str.split("what was popular before _"), name_before_year),
    (str.split("what was popular after _"), name_after_year),
    (str.split("what is %"), desc_by_name),
    (str.split("what rank is %"), rank_by_name),
    (["bye"], bye_action),
]

def search_pa_list(src: List[str]) -> List[str]:
    if src==["bye"]:
        return bye_action("waluigi")
    for i in pa_list:
        if match(i[0],src):
            ans=i[1](match(i[0],src))
            return ["No answers"] if ans==[] else ans
    return ["I don't understand"]

def query_loop() -> None:
    print("Welcome to the meme database!\n")
    while True:
        try:
            print()
            query = input("Your query? ").replace("?", "").lower().split()
            answers = search_pa_list(query)
            for ans in answers:
                print(ans)

        except (KeyboardInterrupt, EOFError):
            break

    print("\nSo long!\n")

query_loop()