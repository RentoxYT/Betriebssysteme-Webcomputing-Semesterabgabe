#!/usr/bin/python3
print('Content-type: text/html \n')

//Listen sind systematisch wie folgt aufgebaut
//Abschluss_Studiengang_Semseter
//z.B. ba_informatik_2

ba_applied_computer_science_1 = ["Einführung in die Informationsverarbeitung", "Einführung in die Praktische Informatik", "Rechnerorganisation", "Mediengestaltung", "Mathematik 1", "Englisch", "Projektorientiertes Studium"]
ba_applied_computer_science_2 = ["Algorithmen und Datenstrukturen", "Interaktive Systeme", "Programmierung 1", "Betriebssysteme/Webcomputing", "Mathematik 2", "Formale Sprachen und Automatentheorie"]
ba_applied_computer_science_3 = ["Grundlagen der Sicherheit", "Datenbanken", "Programmierung 2", "Betriebssysteme/Rechnernetze", "Mathematik 3", "Einführung in das wissenschaftliche Schreiben", "Wahlpflichtmodul"]
ba_applied_computer_science_4 = ["Software Engineering", "Grundlagen der künstlichen Intelligenz", "Programmierung 3", "Komplexpraktikum", "Wahlpflichtmodul", "Wahlpflichtmodul"]
ba_applied_computer_science_5 = ["verpflichtendes Auslandssemester"]
ba_applied_computer_science_6 = ["Betreutes Praxisprojekt", "Praxisseminar", "Bachlorseminar", "Bachlorarbeit mit Kolloquium"]

ba_augenoptik_1 = ["Praktische Einführung in den Ingenieurberuf", "Angewandte Mathematik 1", "Experimentalphysik 1", "Werkstoffkunde", "Subjektive Refraktionsbestimmung 1", "Anatomie und Physiologie"]
ba_augenoptik_2 = ["Technische Optik", "Angewandte Mathematik 2", "Experimentalphysik 2", "Pathologie", "Subjektive Refraktionsbestimmung 2", "Kontaktlinsenanpassung 1"]
ba_augenoptik_3 = ["Optische Gerätetechnik", "Einführung in die Konstruktionslehre", "Einführung in die Elektrotechnik", "Optometrisches Screening 1", "Subjektive Refraktionsbestimmung 3", "Kontaktlinsenanpassung 2"]
ba_augenoptik_4 = ["Opthalmotechnik", "Messtechnik und Sensorik", "Einführung in die Elektronik", "Informatik 1", "Subjektive Refraktionsbestimmung 4", "Kontaktlinsenanpassung 3"]
ba_augenoptik_5 = ["Optikentwicklung", "Optometrisches Screening 2", "Optik & Technologie der Sehhilfen", "Kontaktlinsenanpassung 4", "Wahlpflichtmodul", "Wahlpflichtmodul"]
ba_augenoptik_6 = ["Optikfertigung", "Wissenschaftliches Arbeiten", "Studium Generale", "Wahlpflichtmodul", "Wahlpflichtmodul", "Wahlpflichtmodul"]
ba_augenoptik_7 = ["Praxisphase", "Bachelorarbeit", "Bachelorkolloquium"]

ba_betriebswirtschaftslehre_1 = ["Buchführung", "Wirtschaftsenglisch", "Wirtschaftsrecht", "Volkswirtschaftslehre 1", "Grundlagen unternehmerischen Handelns", "Mathematik/Statistik 1"]
ba_betriebswirtschaftslehre_2 = ["Externes Rechnungswesen und Bilanzen", "Internes Rechnungswesen", "Studium Generale 1", "Volkswirtschaftslehre 2", "Personal und Organisation", "Mathematik/Statistik 2"]
ba_betriebswirtschaftslehre_3 = ["Controlling und Risikomanagement", "Produktions- und Materialwirtschaft", "Marketing", "Finanzierung und Investition", "Projektmanagement", "Wirtschaftsinformatik 1"]
ba_betriebswirtschaftslehre_4 = ["Wahlpflichtmodul BWL", "Wahlpflichtmodul BWL", "Wahlpflichtmodul BWL", "Wahlpflichtmodul VWL/WI", "Business Plan", "Wirtschaftsinformatik 2"]
ba_betriebswirtschaftslehre_5 = ["Wahlpflichtmodul BWL", "Wahlpflichtmodul BWL", "Wahlpflichtmodul BWL", "Wahlpflichtmodul VWL/WI", "Studium Generale 2", "Gründungsmanagement und Nachfolge"]
ba_betriebswirtschaftslehre_6 = ["Betreutes Praxisprojekt mit Praxisarbeit und Praxisseminar", "Bachelor-Arbeit mit Kolloquium und Bachelor-Seminar"]

ba_elektromobilitaet_1 = ["Chemie und Werkstoffe", "Elektrotechnik 1", "Fertigungstechnik 1", "Informatik 1", "Ingenieurmathematik 1", "Konstruktion 1"]
ba_elektromobilitaet_2 = ["Analoge Schaltungen 1", "Elektrotechnik 2", "Technische Mechanik 1", "Informatik 2", "Ingenieurmathematik 2", "Konstruktion 2"]
ba_elektromobilitaet_3 = ["Analoge Schaltungen 2", "Elektrotechnik 3", "Antriebstechnik", "Regel- und Steuerungstechnik", "Ingenieurmathematik 3", "Technische Mechanik 2"]
ba_elektromobilitaet_4 = ["Elektrische Maschinen", "Grundlagen der Mikrocontrollertechnik", "Leistungselektronik", "Logistik", "Technische Sensorik", "Technisches Wahlpflichtmodul"]
ba_elektromobilitaet_5 = ["Elektrische Antriebstechnik", "Interdisziplinäres Projekt 1", "Maschinenelemente 1", "Mobile Energiespeicher", "Technische Mechanik 3", "Technisches Wahlpflichtmodul"]
ba_elektromobilitaet_6 = ["Mechanische Antriebe", "Interdisziplinäres Projekt 2", "Maschinenelemente 2", "Studium Generale", "Nichttechnisches Wahlpflichtmodul", "Technisches Wahlpflichtmodul"]
ba_elektromobilitaet_7 = ["Bachelorarbeit", "Bachelorkolloquium", "Betreute Praxisphase"]

ba_informatik_1 = ["Einführung in die Informationsverarbeitung", "Einführung in die Praktische Informatik", "Rechnerorganisation", "Mediengestaltung", "Mathematik 1", "Englisch", "Projektorientiertes Studium"]
ba_informatik_2 = ["Algorithmen und Datenstrukturen", "Interaktive Systeme", "Programmierung 1", "Betriebssysteme/Webcomputing", "Mathematik 2", "Formale Sprachen und Automatentheorie"]
ba_informatik_3 = ["Grundlagen der Sicherheit", "Datenbanken", "Programmierung 2", "Betriebssysteme/Rechnernetze", "Mathematik 3", "Einführung in das wissenschaftliche Schreiben", "Wahlpflichtmodul"]
ba_informatik_4 = ["Software Engineering", "Grundlagen der künstlichen Intelligenz", "Programmierung 3", "Komplexpraktikum", "Wahlpflichtmodul", "Wahlpflichtmodul"]
ba_informatik_5 = ["Projekt", "Wahlpflichtmodul", "Wahlpflichtmodul", "Wahlpflichtmodul", "Wahlpflichtmodule aus Studium Generale"]
ba_informatik_6 = ["Betreutes Praxisprojekt", "Praxisseminar", "Bachlorseminar", "Bachlorarbeit mit Kolloquium"]

ba_ingenieurinformatik_1 = ["Praktische Einführung in die Ingenieurinformatik", "Angewandte Mathematik 1", "Experimentalphysik 1", "Werkstoffkunde", "Einführung in die Elektrotechnik", "Einführung in die Konstruktionslehre"]
ba_ingenieurinformatik_2 = ["Informatik 1", "Angewandte Mathematik 2", "Experimentalphysik 2", "Digitaltechnik", "Einführung in die Elektronik", "Messtechnik und Sensorik"]
ba_ingenieurinformatik_3 = ["Informatik 2", "Angewandte Mathematik 3", "Datenbanksysteme", "Regelungs- und Steuerungstechnik", "Grundlagen der Mechatronik", "Technische Mechanik 1"]
ba_ingenieurinformatik_4 = ["Eingebettete Systeme und Python", "Grundlagen der Mikrocontrollertechnik", "Signale und Systeme", "IT-Sicherheit und Datenschutz", "Technisches Wahlpflichtmodul", "Technisches Wahlpflichtmodul"]
ba_ingenieurinformatik_5 = ["Applikationsenteicklung für Web und Mobile", "Digitale Bildverarbeitung", "Schaltungs- und Leiterplattenentwurf", "Nichttechnisches Wahlpflichtmodul", "Technisches Wahlpflichtmodul", "Technisches Wahlpflichtmodul"]
ba_ingenieurinformatik_6 = ["Künstliche Intelligenz", "Interdisziplinäres Projekt", "Studium Generale", "Nichttechnisches Wahlpflichtmodul", "Technisches Wahlpflichtmodul", "Technisches Wahlpflichtmodul"]
ba_ingenieurinformatik_7 = ["Praxisphase", "Bachelorarbeit", "Bachelorkolloquium"]
