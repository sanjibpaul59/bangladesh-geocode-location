from dataclasses import dataclass

@dataclass
class Union:
    geo_code: str
    paurasava_code: str
    upazilla_code: str
    district_code: str
    division_code: str
    name: str

@dataclass
class Paurasava:
    geo_code: str
    upazilla_code: str
    district_code: str
    division_code: str
    name: str

@dataclass
class Upazilla:
    geo_code: str
    district_code:str
    division_code: str
    name: str

@dataclass
class District:
    geo_code:str
    division_code: str
    name: str

@dataclass
class Division:
    geo_code: str
    name: str
