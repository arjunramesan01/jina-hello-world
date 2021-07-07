from jina import Executor, Flow, requests

my_json_database = [
    {
        "id":'1',
        "text":'hello world',
        "tags" : {
            "type":'Lo_question'
        }
    },
    {
        "id":'2',
        "text":'good bye',
        "tags" : {
            "type":'Lo_question'
        }
    }
]


# for index
def index():
    f = Flow.load_config('flows/index.yml')
    with f:
        f.index(my_json_database)

# for search
def query():
    f = Flow.load_config('flows/query.yml')
    with f:
        f.block()


index()