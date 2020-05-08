
def finder(files, queries):

    """
    YOUR CODE HERE
    """
    search_results = {}
    for file in files:
        name = file.split('/')[-1]
        if name in search_results:
            search_results[name].append(file)
        else:
            search_results[name] = [file]
    result = []
    for query in queries:
        if query in search_results:
            query_list = search_results[query]
            for item in query_list:
                result.append(item)
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))