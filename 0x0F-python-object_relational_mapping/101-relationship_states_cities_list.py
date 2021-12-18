#!/usr/bin/python3
"""
Prints all State objects and their City objects in a database.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
