class VazitelneInterface:
    def get_vaha_v_kg(self) -> float:
        raise NotImplementedError
    
    def get_cena_za_kg(self) -> float:
        raise NotImplementedError
    
class KusoveInterface:
    def get_pocet_kusu_v_baleni(self) -> int:
        raise NotImplementedError
    
    def get_cena_za_kus(self) -> float:
        raise NotImplementedError
    
    def get_cena_za_baleni(self) -> float:
        raise NotImplementedError
    
class ZlevnitelneInterface:
    def set_sleva(self, sleva: float) -> None:
        raise NotImplementedError
    
    def get_cena_po_sleve(self) -> float:
        raise NotImplementedError