# from memes import meme_db
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



def year_from_name(matches: List[str]) -> List[str]:
    pass


def bye_action(dummy: List[str]) -> None:
    raise KeyboardInterrupt


pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("wen was % popular"), year_from_name),
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
    print("Welcome to the movie database!\n")
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

# query_loop()

if __name__ == "__main__":
    assert sorted(search_pa_list(["when","was","big","chungus","funny"]))==sorted([2018]),"failed year by name"
    print("All tests passed!")