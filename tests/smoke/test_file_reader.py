from utils.file_reader import Filereader

def test_file_reader():

    data = Filereader.read_jason("testdata/users.json")

    print(data)