from sqlmodel import Session

from cards.db import get_engine, Card, Category


if __name__ == "__main__":
    engine = get_engine()

    session = Session(engine)

    with Session(engine) as session:
        german = Category(name="German")
        basic_german = Category(name="Basic German")
        german_verbs = Category(name="German Verbs")
        french = Category(name="French")
        stats = Category(name="Statistics")
        captials = Category(name="Capitals")
        country_capitals = Category(name="Country Capitals")

        cards = [
            # Create some basic german cards
            Card(front="hello", back="hallo", categories=[german, basic_german]),
            Card(front="goodbye", back="Auf Wiedersehen", categories=[german, basic_german]),
            Card(front="good morning", back="Guten Morgen", categories=[german, basic_german]),
            Card(front="good evening", back="Guten Abend", categories=[german, basic_german]),
            Card(front="good night", back="Gute Nacht", categories=[german, basic_german]),
            Card(front="good day", back="Guten Tag", categories=[german, basic_german]),
            Card(front="how are you?", back="Wie geht es dir?", categories=[german, basic_german]),
            Card(front="I'm fine", back="Es geht mir gut", categories=[german, basic_german]),
            Card(front="I'm not well", back="Es geht mir nicht gut", categories=[german, basic_german]),
            Card(front="what's your name?", back="Wie heißt du?", categories=[german, basic_german]),
            Card(front="my name is", back="Ich heiße", categories=[german, basic_german]),
            Card(front="I'm from ...", back="Ich komme aus ...", categories=[german, basic_german]),
            Card(front="I'm ... years old", back="Ich bin ... Jahre alt", categories=[german, basic_german]),
            Card(front="I'm a student", back="Ich bin Student", categories=[german, basic_german]),
            Card(front="I'm a teacher", back="Ich bin Lehrer", categories=[german, basic_german]),
            Card(front="yes", back="ja", categories=[german, basic_german]),
            Card(front="no", back="nein", categories=[german, basic_german]),
            Card(front="please", back="bitte", categories=[german, basic_german]),
            Card(front="thank you", back="danke", categories=[german, basic_german]),
            Card(front="you're welcome", back="bitte schön", categories=[german, basic_german]),
            Card(front="excuse me", back="entschuldigung", categories=[german, basic_german]),
            Card(front="I'm sorry", back="es tut mir leid", categories=[german, basic_german]),
            Card(front="I don't understand", back="Ich verstehe nicht", categories=[german, basic_german]),
            Card(front="I don't speak German", back="Ich spreche kein Deutsch", categories=[german, basic_german]),
            Card(front="I don't speak German", back="Ich kann kein Deutsch", categories=[german, basic_german]),
            # Create some german verb cards
            Card(front="to be", back="sein", categories=[german, german_verbs]),
            Card(front="to eat", back="essen", categories=[german, german_verbs]),
            Card(front="to sit", back="sitzen", categories=[german, german_verbs]),
            Card(front="to sleep", back="schlafen", categories=[german, german_verbs]),
            # French cards
            Card(front="hello", back="bonjour", categories=[french]),
            Card(front="goodbye", back="au revoir", categories=[french]),
            Card(front="good morning", back="bonjour", categories=[french]),
            Card(front="good evening", back="bonsoir", categories=[french]),
            Card(front="good night", back="bonne nuit", categories=[french]),
            Card(front="good day", back="bonne journée", categories=[french]),
            Card(front="how are you?", back="comment allez-vous?", categories=[french]),
            Card(front="I'm fine", back="je vais bien", categories=[french]),
            Card(front="I'm not well", back="je ne vais pas bien", categories=[french]),
            Card(front="what's your name?", back="comment vous appelez-vous?", categories=[french]),
            Card(front="my name is ...", back="je m'appelle ...", categories=[french]),
            # Other 
            Card(front="P[A | B]", back="P[B | A] * P[A] / P[B]", categories=[stats]),
            # Country capitals
            Card(front="Afghanistan", back="Kabul", categories=[country_capitals]),
            Card(front="Albania", back="Tirana", categories=[country_capitals]),
            Card(front="Algeria", back="Algiers", categories=[country_capitals]),
            Card(front="Andorra", back="Andorra la Vella", categories=[country_capitals]),
            Card(front="Angola", back="Luanda", categories=[country_capitals]),
            Card(front="Antigua and Barbuda", back="Saint John's", categories=[country_capitals]),
            Card(front="Argentina", back="Buenos Aires", categories=[country_capitals]),
            Card(front="Armenia", back="Yerevan", categories=[country_capitals]),
            Card(front="Australia", back="Canberra", categories=[country_capitals]),
            Card(front="Austria", back="Vienna", categories=[country_capitals]),
            Card(front="Azerbaijan", back="Baku", categories=[country_capitals]),
            Card(front="Bahamas", back="Nassau", categories=[country_capitals]),
            Card(front="Bahrain", back="Manama", categories=[country_capitals]),
            Card(front="Bangladesh", back="Dhaka", categories=[country_capitals]),
            Card(front="Barbados", back="Bridgetown", categories=[country_capitals]),
            Card(front="Belarus", back="Minsk", categories=[country_capitals]),
            Card(front="Belgium", back="Brussels", categories=[country_capitals]),
            Card(front="Belize", back="Belmopan", categories=[country_capitals]),
            Card(front="Benin", back="Porto-Novo", categories=[country_capitals]),
            Card(front="Bhutan", back="Thimphu", categories=[country_capitals]),
            Card(front="Bolivia", back="Sucre", categories=[country_capitals]),
            Card(front="Bosnia and Herzegovina", back="Sarajevo", categories=[country_capitals]),
            Card(front="Botswana", back="Gaborone", categories=[country_capitals]),
            Card(front="Brazil", back="Brasília", categories=[country_capitals]),
            Card(front="Brunei", back="Bandar Seri Begawan", categories=[country_capitals]),
            Card(front="Bulgaria", back="Sofia", categories=[country_capitals]),
            Card(front="Burkina Faso", back="Ouagadougou", categories=[country_capitals]),
            Card(front="Burundi", back="Gitega", categories=[country_capitals]),
            Card(front="Cabo Verde", back="Praia", categories=[country_capitals]),
            Card(front="Cambodia", back="Phnom Penh", categories=[country_capitals]),
            Card(front="Cameroon", back="Yaoundé", categories=[country_capitals]),
            # More to come
            # Capitals of US states
            Card(front="Alabama", back="Montgomery", categories=[captials]),
            Card(front="Alaska", back="Juneau", categories=[captials]),
            Card(front="Arizona", back="Phoenix", categories=[captials]),
            Card(front="Arkansas", back="Little Rock", categories=[captials]),
            Card(front="California", back="Sacramento", categories=[captials]),
            Card(front="Colorado", back="Denver", categories=[captials]),
            Card(front="Connecticut", back="Hartford", categories=[captials]),
            Card(front="Delaware", back="Dover", categories=[captials]),
            Card(front="Florida", back="Tallahassee", categories=[captials]),
            Card(front="Georgia", back="Atlanta", categories=[captials]),
            Card(front="Hawaii", back="Honolulu", categories=[captials]),
            Card(front="Idaho", back="Boise", categories=[captials]),
            Card(front="Illinois", back="Springfield", categories=[captials]),
            Card(front="Indiana", back="Indianapolis", categories=[captials]),
            Card(front="Iowa", back="Des Moines", categories=[captials]),
            Card(front="Kansas", back="Topeka", categories=[captials]),
            Card(front="Kentucky", back="Frankfort", categories=[captials]),
            Card(front="Louisiana", back="Baton Rouge", categories=[captials]),
            Card(front="Maine", back="Augusta", categories=[captials]),
            Card(front="Maryland", back="Annapolis", categories=[captials]),
            Card(front="Massachusetts", back="Boston", categories=[captials]),
            Card(front="Michigan", back="Lansing", categories=[captials]),
            Card(front="Minnesota", back="Saint Paul", categories=[captials]),
            Card(front="Mississippi", back="Jackson", categories=[captials]),
            Card(front="Missouri", back="Jefferson City", categories=[captials]),
            Card(front="Montana", back="Helena", categories=[captials]),
            Card(front="Nebraska", back="Lincoln", categories=[captials]),
            Card(front="Nevada", back="Carson City", categories=[captials]),
            Card(front="New Hampshire", back="Concord", categories=[captials]),
            Card(front="New Jersey", back="Trenton", categories=[captials]),
            Card(front="New Mexico", back="Santa Fe", categories=[captials]),
            Card(front="New York", back="Albany", categories=[captials]),
            Card(front="North Carolina", back="Raleigh", categories=[captials]),
            Card(front="North Dakota", back="Bismarck", categories=[captials]),
            Card(front="Ohio", back="Columbus", categories=[captials]),
            Card(front="Oklahoma", back="Oklahoma City", categories=[captials]),
            Card(front="Oregon", back="Salem", categories=[captials]),
            Card(front="Pennsylvania", back="Harrisburg", categories=[captials]),
            Card(front="Rhode Island", back="Providence", categories=[captials]),
            Card(front="South Carolina", back="Columbia", categories=[captials]),
            Card(front="South Dakota", back="Pierre", categories=[captials]),
            Card(front="Tennessee", back="Nashville", categories=[captials]),
            Card(front="Texas", back="Austin", categories=[captials]),
            Card(front="Utah", back="Salt Lake City", categories=[captials]),
            Card(front="Vermont", back="Montpelier", categories=[captials]),
            Card(front="Virginia", back="Richmond", categories=[captials]),
            Card(front="Washington", back="Olympia", categories=[captials]),
            Card(front="West Virginia", back="Charleston", categories=[captials]),
            Card(front="Wisconsin", back="Madison", categories=[captials]),
            Card(front="Wyoming", back="Cheyenne", categories=[captials]),
        ]
        for card in cards:
            session.add(card)

        session.commit()