from Domain.ProdusValidator import ProdusValidator
from Repository.json_repository import JsonRepository
from Service.produsService import ProdusService
from UI.console import Console


def main():
    produsRepository = JsonRepository("produs.json")
    produsValidator = ProdusValidator()

    produsService = ProdusService(produsRepository,produsValidator)

    console = Console(produsService)

    console.runMenu()




if __name__ == '__main__':
    main()