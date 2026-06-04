#!/usr/bin/python3

import cgi
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

ba_ingenieurwissenschaften_1 = ["Grundlagen der Elektrotechnik 1", "Werkstoffkunde", "Einführung in die Konstruktionslehre", "Experimentalphysik 1", "Angewandte Mathematik 1", "Technische Mechanik 1"]
ba_ingenieurwissenschaften_2 = ["Grundlagen der Elektrotechnik 2", "Grundlagen der Elektronik 1", "Messtechnik und Sensorik", "Experimentalphysik 2", "Angewandte Mathematik 2", "Informatik 1"]
ba_ingenieurwissenschaften_3 = ["Grundlagen der Elektrotechnik 3", "Grundlagen der Elektronik 2", "Regelungs- und Steuerungstechnik", "Schaltungs- und Leiterplattenentwurf", "Angewandte Mathematik 3", "Informatik 2"]
ba_ingenieurwissenschaften_4 = ["Elektrische Maschinen", "Leistungselektronik", "Signale und Systeme", "Digitaltechnik", "Automatisieren mit SPS", "Grundlagen der Mikrocontrollertechnik"]
ba_ingenieurwissenschaften_5 = ["Elektrische Antriebe", "Optische Kommunikationstechnik", "Grundlagen der Mechatronik", "Technisches Wahlpflichtmodul", "Technisches Wahlpflichtmodul", "Nichttechnisches Wahlpflichtmodul"]
ba_ingenieurwissenschaften_6 = ["Simulations- und Regelungstechnik", "Systemdynamik für Mechatronik", "InterdisziplinÃ¤res Projekt", "Technisches Wahlpflichtmodul", "Technisches Wahlpflichtmodul", "Nichttechnisches Wahlpflichtmodul"]
ba_ingenieurwissenschaften_7 = ["Praxisphase", "Bachelorarbeit", "Bachelorkolloquium"]

ba_it_sicherheit_1 = ["Grundlagen der Mathematik", "Grundlagen der Programmierung 1", "Einführung in die Informatik", "Digitaler Selbstschutz", "Computerarchitektur und Betriebssysteme", "Kommunikation, Führung und Selbstmanagement"]
ba_it_sicherheit_2 = ["Grundlagen der Kryptographie", "Grundlagen der Programmierung 2", "Theoretische Informatik", "Grundlagen der IT-Sicherheit", "Rechnernetze Grundlagen", "English for Computer Scientists"]
ba_it_sicherheit_3 = ["Datenbanken", "Algorithmen und Datenstrukturen", "Angewandte Kryptographie", "Internet-Technologie", "Netzwerksicherheit", "Sicherheitsmanagement"]
ba_it_sicherheit_4 = ["Softwaretechnik", "Entwicklung sicherer Softwaresysteme", "Hardware-Sicherheit", "IT-Forensik", "Einführung in wissenschaftliche Projektarbeit", "Ethik in der IT-Sicherheit"]
ba_it_sicherheit_5 = ["Praxisprojekt", "IT-Recht", "Wahlpflichtfach", "Wahlpflichtfach"]
ba_it_sicherheit_6 = ["Betriebswirtschaftslehre", "Wahlpflichtfach", "Wahlpflichtfach", "Bachelor-Seminar/Kolloquium", "Bachelor-Arbeit"]

ba_maschinenbau_1 = ["Praktische Einführung in den Ingenieurberuf", "Werkstoffkunde", "Einführung in die Konstruktionslehre", "Experimentalphysik 1", "Angewandte Mathematik 1", "Technische Mechanik 1"]
ba_maschinenbau_2 = ["Thermodynamik", "Werkstoffkunde 2", "Erweiterte Konstruktionslehre", "Informatik 1", "Angewandte Mathematik 2", "Technische Mechanik 2"]
ba_maschinenbau_3 = ["Fertigungstechnik 1", "Maschinenelemente 1", "Einführung in die Elektrotechnik", "Wärme- und Stoffübertragung", "Angewandte Mathematik 3", "Technische Mechanik 3"]
ba_maschinenbau_4 = ["Fertigungstechnik 2", "Maschinenelemente 2", "Einführung in die Elektronik", "Messtechnik und Sensorik", "Finite Elemente Methode", "Strömungslehre"]
ba_maschinenbau_5 = ["Antriebstechnik", "Betriebswirtschaftslehre 1", "Regelungs- und Steuerungstechnik", "Kreislaufwirtschaft und Recycling-Technologien", "Technisches Wahlpflichtmodul", "Freies Wahlpflichtmodul"]
ba_maschinenbau_6 = ["Interdisziplinäres Projekt", "Automatisierungstechnik", "Wissenschaftliches Arbeiten", "Technisches Wahlpflichtmodul", "Freies Wahlpflichtmodul", "Studium Generale"]
ba_maschinenbau_7 = ["Praxisphase", "Bachelorarbeit", "Bachelorkolloquium"]

ba_medieninformatik_1 = ["Grundlagen der Mathematik", "Grundlagen der Programmierung 1", "Einführung in die Informatik", "Mediendesign 1", "Computerarchitektur und Betriebssysteme", "Kommunikation, Führung und Selbstmanagement"]
ba_medieninformatik_2 = ["Relationen und Funktionen", "Grundlagen der Programmierung 2", "Theoretische Informatik", "Mediendesign 2", "Rechnernetze Grundlagen", "Mensch-Computer-Interaktionen"]
ba_medieninformatik_3 = ["Datenbanken", "Algorithmen und Datenstrukturen", "Web-Programmierung", "Computergrafik", "Multimediatechnik", "Projektmanagement"]
ba_medieninformatik_4 = ["Softwaretechnik", "Internetserver-Programmierung", "Internet Anwendungen für mobile Geräte", "IT-Recht", "Einführung in wissenschaftliche Projektarbeit", "Grundlagen der IT-Sicherheit"]
ba_medieninformatik_5 = ["Praxisprojekt", "Pattern and Frameworks", "Wahlpflichtfach", "Wahlpflichtfach"]
ba_medieninformatik_6 = ["Betriebswirtschaftslehre", "Wahlpflichtfach", "Wahlpflichtfach", "Bachelor-Seminar/Kolloquium", "Bachelor-Arbeit"]

ba_medizininformatik_1 = ["Mathematik 1", "Einführung in die Praktische Informatik", "Einführung in die Informationsverarbeitung", "Medizin 1", "Englisch", "Projektorientiertes Studium"]
ba_medizininformatik_2 = ["Mathematik 2", "Programmierung 1", "Algorithmen und Datenstrukturen", "Medizin 2", "Betriebssysteme/Webcomputing", "Grundlagen der Medizininformatik"]
ba_medizininformatik_3 = ["Datenbanken", "Programmierung 2", "Digitales Gesundheitssystem", "Biometrie und Statistik", "Betriebssysteme/Rechnernetze", "Grundlagen der Sicherheit", "Einführung in das wissenschaftliche Schreiben"]
ba_medizininformatik_4 = ["Software Engineering", "Software-Bewertung und -Auswahl", "Interoperabilität im Gesundheitswesen", "Grundlagen der Künstlichen Intelligenz", "Komplexpraktikum", "Wahlpflichtmodul"]
ba_medizininformatik_5 = ["Medizinische Prozesse und IT-Systeme", "Projekt", "Wahlpflichtmodul", "Wahlpflichtmodul", "Wahlpflichtmodule aus dem Studium Generale"]
ba_medizininformatik_6 = ["Praxisprojekt", "Praxisseminar", "Bachelorseminar", "Bachelorarbeit mit Kolloquium"]

ba_wirtschaftsinformatik_1 = ["Grundlagen der Wirtschafts- und Finanzmathematik", "Grundlagen der Wirtschaftswissenschaften", "Algorithmen und Datenstrukturen", "Grundlagen und Wirkung der Wirtschaftsinformatik", "Betriebssysteme und Netzwerke", "Projektstudium und Wissenschaftliches Arbeiten"]
ba_wirtschaftsinformatik_2 = ["Grundlagen der Prozessmodellierung", "Grundlagen statistischer Methoden", "Objektorientierter Systementwurf", "Englisch anwenden in der Wirtschaftsinformatik", "Rechnungswesen und Controlling", "Datenbanken - Modellierung und Strukturierung"]
ba_wirtschaftsinformatik_3 = ["Systemanalyse", "Softwareengineering", "Datenbanken - Anwendung und Entwicklung", "Usability & Software-Ergonomie", "Businessplan-Wettbewerb", "Projektmanagement und soziale Kompetenzen"]
ba_wirtschaftsinformatik_4 = ["Systemarchitekturen und -integration", "Auswahl und Anpassung von IT-Diensten", "Management und Organisation", "DV-orientiertes Wirtschaftsrecht", "Predictive Analysis and Big Data", "Wahlpflichtmodul"]
ba_wirtschaftsinformatik_5 = ["Informationsmanagement", "Produktion, Logistik und Vertrieb", "Datenschutz und Sicherheit", "Studium Generale: Forschungsansätze in der WI", "Wahlpflichtmodul", "Wahlpflichtmodul Wirtschaft"]
ba_wirtschaftsinformatik_6 = ["Betreutes Praxisprojekt", "Praxisseminar", "Bachelorseminar", "Bachelorarbeit (mit Kolloquium)"]

ba_wirtschaftsingenieurwesen_1 = ["Grundlagen der Elektrotechnik 1", "Praktische Einführung in den Ingenieurberuf", "Betriebswirtschaftslehre 1", "Experimentalphysik 1", "Angewandte Mathematik 1", "Rechnungswesen 1"]
ba_wirtschaftsingenieurwesen_2 = ["Grundlagen der Elektrotechnik 2", "Betriebswirtschaftslehre 2", "Rechnungswesen 2", "Experimentalphysik 2", "Angewandte Mathematik 2", "Informatik 1"]
ba_wirtschaftsingenieurwesen_3 = ["Werkstoffkunde", "Technische Mechanik 1", "Betriebswirtschaftslehre 3", "Einführung in die Konstruktionslehre", "Angewandte Mathematik 3", "Projektmanagement"]
ba_wirtschaftsingenieurwesen_4 = ["Betriebswirtschaftslehre 4", "Messtechnik und Sensorik", "Wirtschaftsrecht", "Volkswirtschaftslehre", "Betriebswirtschaftliches Wahlpflichtmodul", "Technisches Wahlpflichtmodul"]
ba_wirtschaftsingenieurwesen_5 = ["ERP für Wirtschaftsingenieure", "Statistische Methoden", "Informatik 2", "Betriebswirtschaftliches Wahlpflichtmodul", "Technisches Wahlpflichtmodul", "Technisches Wahlpflichtmodul"]
ba_wirtschaftsingenieurwesen_6 = ["Wissenschaftliches Arbeiten", "Interdisziplinäres Projekt", "Betriebswirtschaftliches Wahlpflichtmodul", "Technisches Wahlpflichtmodul", "Technisches Wahlpflichtmodul", "Studium Generale (Wahlpflichtmodul)"]
ba_wirtschaftsingenieurwesen_7 = ["Praxisphase", "Bachelorarbeit", "Bachelorkolloquium"]

ma_betriebswirtschaftslehre_1 = ["International Financial Reporting Standards (IFRS)", "Quantitative Tools - Applied Econometrics", "Wahlpflichtmodul", "Wahlpflichtmodul", "Wahlpflichtmodul"]
ma_betriebswirtschaftslehre_2 = ["Strategisches Management & Marketing", "Global Economics", "Wahlpflichtmodul", "Wahlpflichtmodul", "Wahlpflichtmodul"]
ma_betriebswirtschaftslehre_3 = ["Auslandssemester oder Inlandssemester (BWL-Projekt und 3 Wahlpflichtmodule)"]
ma_betriebswirtschaftslehre_4 = ["Integratives Projekt", "Masterarbeit mit Kolloquium und Master-Seminar"]

ma_digitalisierung_und_management_1 = ["Innovationsmanagement", "Analyse und Modellierung von Prozessen", "Nachhaltigkeitsmanagement", "Dokumenten- und Workflowmanagement"]
ma_digitalisierung_und_management_2 = ["Vertriebsmanagement", "Angewandte Data Analytics", "Compliance Management/Corporate Governance", "IT-Projektmanagement"]
ma_digitalisierung_und_management_3 = ["Customer Relationship Management", "Enterprise Knowledge Engineering", "Wahlpflichtmodul", "Wahlpflichtmodul"]
ma_digitalisierung_und_management_4 = ["Angewandtes Change Management", "Wahlpflichtmodul", "Wahlpflichtmodul", "Wahlpflichtmodul"]
ma_digitalisierung_und_management_5 = ["Masterseminar", "Masterarbeit", "Kolloquium"]

ma_energieeffizienz_technischer_systeme_1 = ["Energie- und Ressourcenmanagement", "Mathematische Optimierung", "Energiespeicher", "Wahlpflichtmodul", "Wahlpflichtmodul"]
ma_energieeffizienz_technischer_systeme_2 = ["Angewandte Multidisziplinäre Designoptimierung", "Sicherheit und Zuverlässigkeit", "Wissenschaftliche Projektarbeit", "Wahlpflichtmodul", "Wahlpflichtmodul"]
ma_energieeffizienz_technischer_systeme_3 = ["Masterarbeit", "Kolloquium zur Masterarbeit"]

ma_informatik_1 = ["Mathematik", "Softwarearchitektur und Qualitätssicherung", "Fortgeschrittenes Projektmanagement", "Projekt 1", "Vertiefungsmodul 1", "Wahlpflichtmodul"]
ma_informatik_2 = ["Künstliche Intelligenz", "Datenbanken und Informationssysteme", "Wissenschaftliches Arbeiten: Recherchieren, Schreiben, Präsentieren", "Projekt 2", "Vertiefungsmodul 2", "Wahlpflichtmodul"]
ma_informatik_3 = ["Informatiktheorie", "Entrepreneurship", "Projekt 3", "Vertiefungsmodul 3", "Wahlpflichtmodul", "Wahlpflichtmodul"]
ma_informatik_4 = ["Masterseminar", "Masterarbeit (mit Kolloquium)"]

ma_interactive_media_1 = ["Media theories", "Creative technologies", "Project Management", "Project I", "Elective", "Elective", "German course"]
ma_interactive_media_2 = ["Media research", "Immersive media", "Mobile user experience", "Scientific writing", "Project II", "Elective", "German course"]
ma_interactive_media_3 = ["Media communication", "Interface design", "Entrepreneurship", "Project III", "Elective", "Elective", "German course"]
ma_interactive_media_4 = ["Master thesis with colloquium"]

ma_mechanical_engineering_1 = ["Drive Dynamics and Simulation of Kinematic Systems", "Mathematical Optimization", "Energy and Resource Management", "Elective Module", "Elective Module"]
ma_mechanical_engineering_2 = ["Material Selection and Design Optimization", "Development of Fault Tolerant Software for Embedded Realtime Systems", "Scientific Project", "Elective Module", "Elective Module"]
ma_mechanical_engineering_3 = ["Master Thesis", "Master Colloquium"]

ma_medieninformatik_1 = ["Informationsarchitektur", "User Experience", "Mediendidaktik und Konzeption", "Motion Design", "Moderne Softwareentwicklung", "Künstliche Intelligenz"]
ma_medieninformatik_2 = ["Wahrscheinlichkeitsrechnung und Kryptographie", "Codierung multimedialer Daten", "Wissenschaftliches Seminar", "Wahlpflichtfach", "Wahlpflichtfach", "Wahlpflichtfach"]
ma_medieninformatik_3 = ["Projekt- und Qualitätsmanagement", "Gründungsmanagement", "Wissenschaftliches Projekt", "Wahlpflichtfach", "Wahlpflichtfach", "Wahlpflichtfach"]
ma_medieninformatik_4 = ["Masterseminar", "Masterarbeit und Kolloquium"]

ma_photonik_1 = ["Messtechnik und Instrumentierung", "Mathematische Methoden", "Mikrotechnologien", "Struktur der Materie", "Technische Optik 1", "Theoretische Grundlagen der Photonik 1"]
ma_photonik_2 = ["Forschungs- und Entwicklungsprojekt 1", "Lasertechnik", "Optische Mess- und Analseverfahren", "Technische Optik 2", "Wahlpflichtmodul"]
ma_photonik_3 = ["Forschungs- und Entwicklungsprojekt 2", "Lasermaterialbearbeitung", "Angewandte Photonik", "Management", "Theoretische Grundlagen der Photonik 2", "Wahlpflichtmodul"]
ma_photonik_4 = ["Masterarbeit"]

ma_security_management_1 = ["Grundlagen des Security Managements", "Recht, Compliance und Datenschutz", "Netzwerksicherheit", "Mathematische und technische Grundlagen der IT-Sicherheit", "Sichere IKT-Infrastrukturen und IT-Dienste 1", "Wissenschaftliches Schreiben 1"]
ma_security_management_2 = ["Security- und Krisenmanagement im internationalen Kontext", "Organisatorische Aspekte des Sicherheitsmanagements", "Sichere IKT-Infrastrukturen und IT-Dienste 2", "Secure System Lifecycle Management", "Wissenschaftliches Schreiben 1", "Projekt"]
ma_security_management_3 = ["Wahlpflichtmodul", "Wahlpflichtmodul", "Wahlpflichtmodul", "Masterarbeit (mit Kolloquium)"]

ma_technologie_und_innovationsmanagement_und_entrepreneurship_1 = ["BWL-Management & Businessplan", "Technologiemanagement", "Innovationsmanagement", "Lab 1: Technologie-Vorausschau", "Produktkalkulation & FuE-Controlling"]
ma_technologie_und_innovationsmanagement_und_entrepreneurship_2 = ["VWL-Technologiepolitik", "Innovation Intelligence/Innovationsmarktforschung", "Gründungsmanagement & Entreneurial Marketing", "Lab 2: Produktplanung und Konzeptentwicklung", "Personalführung und Teammanagement"]
ma_technologie_und_innovationsmanagement_und_entrepreneurship_3 = ["Integratives Projekt", "Masterseminar", "Masterarbeit und Kolloquium"]

ma_wirtschaftsinformatik_1 = ["Unternehmensführung", "Wertorientiertes IT-Management", "Theorie der Informatik", "Advanced Software Engineering", "Modellierung und Analyse von Prozessen"]
ma_wirtschaftsinformatik_2 = ["Security Management", "Management Kooperativer Prozesse", "Implementierung von Prozessen", "Wahlpflichtmodul", "Wahlpflichtmodul"]
ma_wirtschaftsinformatik_3 = ["IT-Recht", "eCommerce", "Wahlpflichtmodul", "Wahlpflichtmodul", "Wahlpflichtmodul"]
ma_wirtschaftsinformatik_4 = ["Masterseminar", "Masterarbeit (mit Kolloquium)"]

studiengaenge = {

    "Applied Computer Science": {
        "1": ba_applied_computer_science_1,
        "2": ba_applied_computer_science_2,
        "3": ba_applied_computer_science_3,
        "4": ba_applied_computer_science_4,
        "5": ba_applied_computer_science_5,
        "6": ba_applied_computer_science_6
    },

    "Augenoptik": {
        "1": ba_augenoptik_1,
        "2": ba_augenoptik_2,
        "3": ba_augenoptik_3,
        "4": ba_augenoptik_4,
        "5": ba_augenoptik_5,
        "6": ba_augenoptik_6,
        "7": ba_augenoptik_7
    },

    "Betriebswirtschaftslehre": {
        "1": ba_betriebswirtschaftslehre_1,
        "2": ba_betriebswirtschaftslehre_2,
        "3": ba_betriebswirtschaftslehre_3,
        "4": ba_betriebswirtschaftslehre_4,
        "5": ba_betriebswirtschaftslehre_5,
        "6": ba_betriebswirtschaftslehre_6
    },

    "Elektromobilität": {
        "1": ba_elektromobilitaet_1,
        "2": ba_elektromobilitaet_2,
        "3": ba_elektromobilitaet_3,
        "4": ba_elektromobilitaet_4,
        "5": ba_elektromobilitaet_5,
        "6": ba_elektromobilitaet_6,
        "7": ba_elektromobilitaet_7
    },

    "Informatik": {
        "1": ba_informatik_1,
        "2": ba_informatik_2,
        "3": ba_informatik_3,
        "4": ba_informatik_4,
        "5": ba_informatik_5,
        "6": ba_informatik_6
    },

    "Ingenieurinformatik": {
        "1": ba_ingenieurinformatik_1,
        "2": ba_ingenieurinformatik_2,
        "3": ba_ingenieurinformatik_3,
        "4": ba_ingenieurinformatik_4,
        "5": ba_ingenieurinformatik_5,
        "6": ba_ingenieurinformatik_6,
        "7": ba_ingenieurinformatik_7
    },

    "Ingenieurwissenschaften": {
        "1": ba_ingenieurwissenschaften_1,
        "2": ba_ingenieurwissenschaften_2,
        "3": ba_ingenieurwissenschaften_3,
        "4": ba_ingenieurwissenschaften_4,
        "5": ba_ingenieurwissenschaften_5,
        "6": ba_ingenieurwissenschaften_6,
        "7": ba_ingenieurwissenschaften_7
    },

    "IT-Sicherheit": {
        "1": ba_it_sicherheit_1,
        "2": ba_it_sicherheit_2,
        "3": ba_it_sicherheit_3,
        "4": ba_it_sicherheit_4,
        "5": ba_it_sicherheit_5,
        "6": ba_it_sicherheit_6
    },

    "Maschinenbau": {
        "1": ba_maschinenbau_1,
        "2": ba_maschinenbau_2,
        "3": ba_maschinenbau_3,
        "4": ba_maschinenbau_4,
        "5": ba_maschinenbau_5,
        "6": ba_maschinenbau_6,
        "7": ba_maschinenbau_7
    },

    "Medieninformatik": {
        "1": ba_medieninformatik_1,
        "2": ba_medieninformatik_2,
        "3": ba_medieninformatik_3,
        "4": ba_medieninformatik_4,
        "5": ba_medieninformatik_5,
        "6": ba_medieninformatik_6
    },

    "Medizininformatik": {
        "1": ba_medizininformatik_1,
        "2": ba_medizininformatik_2,
        "3": ba_medizininformatik_3,
        "4": ba_medizininformatik_4,
        "5": ba_medizininformatik_5,
        "6": ba_medizininformatik_6
    },

    "Wirtschaftsinformatik": {
        "1": ba_wirtschaftsinformatik_1,
        "2": ba_wirtschaftsinformatik_2,
        "3": ba_wirtschaftsinformatik_3,
        "4": ba_wirtschaftsinformatik_4,
        "5": ba_wirtschaftsinformatik_5,
        "6": ba_wirtschaftsinformatik_6
    },

    "Wirtschaftsingenieurwesen": {
        "1": ba_wirtschaftsingenieurwesen_1,
        "2": ba_wirtschaftsingenieurwesen_2,
        "3": ba_wirtschaftsingenieurwesen_3,
        "4": ba_wirtschaftsingenieurwesen_4,
        "5": ba_wirtschaftsingenieurwesen_5,
        "6": ba_wirtschaftsingenieurwesen_6,
        "7": ba_wirtschaftsingenieurwesen_7
    }

}

master_studiengaenge = {

    "Digitalisierung und Management": {
        "1": ma_digitalisierung_und_management_1,
        "2": ma_digitalisierung_und_management_2,
        "3": ma_digitalisierung_und_management_3,
        "4": ma_digitalisierung_und_management_4,
        "5": ma_digitalisierung_und_management_5
    },

    "Energieeffizienz technischer Systeme": {
        "1": ma_energieeffizienz_technischer_systeme_1,
        "2": ma_energieeffizienz_technischer_systeme_2,
        "3": ma_energieeffizienz_technischer_systeme_3
    },

    "Informatik": {
        "1": ma_informatik_1,
        "2": ma_informatik_2,
        "3": ma_informatik_3,
        "4": ma_informatik_4
    },

    "Interactive Media": {
        "1": ma_interactive_media_1,
        "2": ma_interactive_media_2,
        "3": ma_interactive_media_3,
        "4": ma_interactive_media_4
    },

    "Mechanical Engineering": {
        "1": ma_mechanical_engineering_1,
        "2": ma_mechanical_engineering_2,
        "3": ma_mechanical_engineering_3
    },

    "Medieninformatik": {
        "1": ma_medieninformatik_1,
        "2": ma_medieninformatik_2,
        "3": ma_medieninformatik_3,
        "4": ma_medieninformatik_4
    },

    "Photonik": {
        "1": ma_photonik_1,
        "2": ma_photonik_2,
        "3": ma_photonik_3,
        "4": ma_photonik_4
    },

    "Security Management": {
        "1": ma_security_management_1,
        "2": ma_security_management_2,
        "3": ma_security_management_3
    },

    "Technologie- und Innovationsmanagement und Entrepreneurship": {
        "1": ma_technologie_und_innovationsmanagement_und_entrepreneurship_1,
        "2": ma_technologie_und_innovationsmanagement_und_entrepreneurship_2,
        "3": ma_technologie_und_innovationsmanagement_und_entrepreneurship_3
    },

    "Wirtschaftsinformatik": {
        "1": ma_wirtschaftsinformatik_1,
        "2": ma_wirtschaftsinformatik_2,
        "3": ma_wirtschaftsinformatik_3,
        "4": ma_wirtschaftsinformatik_4
    }
}

form = cgi.FieldStorage()
matrikelnummer = form.getvalue("Matrikelnummer")
studiengang = form.getvalue("Studiengang")
semester = form.getvalue("Semester")
studienart = form.getvalue("Studienart")


module = []

if studienart == "Bachelor":
    if studiengang in studiengaenge:
        if semester in studiengaenge[studiengang]:
            module = studiengaenge[studiengang][semester]

elif studienart == "Master":

    if studiengang in master_studiengaenge:
        if semester in master_studiengaenge[studiengang]:
            module = master_studiengaenge[studiengang][semester]

module_html = ""

if len(module) == 0:
  module_html = """
    <li class="list-group-item text-danger">
        Keine Module gefunden
    </li>
    """
else:
  for modul in module:
    module_html += f"""
    <li class="list-group-item">
        {modul}
    </li>
    """


print("Content-type: text/html")
print()

print(f"""
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
        <meta name="viewport"
          content="width=device-width, initial-scale=1.0">
    <title>Ausgabe</title>
        <link rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css">

    <link rel="stylesheet"
          href="../Betriebssysteme-Webcomputing-Semesterabgabe/css/main.css">
</head>
<body>

<div class="container mt-5">

    <div class="col-md-6 mx-auto">

        <div class="card p-4 shadow">

            <h1 class="text-center mb-4">
                Eingegebene Daten
            </h1>

            <ul class="list-group">

                <li class="list-group-item">
                    Matrikelnummer: {matrikelnummer}
                </li>

                <li class="list-group-item">
                    Studiengang: {studiengang}
                </li>

                <li class="list-group-item">
                    Semester: {semester}
                </li>

                <li class="list-group-item">
                    Studienart: {studienart}
                </li>

            </ul>
	</div>

<div class="card p-4 shadow mt-4">

    <h2 class="text-center mb-4">
        Module dieses Semester
    </h2>

    <ul class="list-group">
        {module_html}
    </ul>
     <div class="text-center mt-4">
        <a href="../Betriebssysteme-Webcomputing-Semesterabgabe/index.html" class="btn btn-primary">
            Zurück zur Auswahl
        </a>
    </div>
</div>
    </div>
</div>
<footer class="bg-body-tertiary text-center mt-auto">

    <div class="text-center p-3"
         style="background-color: rgba(0, 0, 0, 0.05);">

        GitHub Paul Sohnrey & Vanessa Folte:

        <a class="text-reset fw-bold"
           href="https://github.com/RentoxYT/Betriebssysteme-Webcomputing-Semesterabgabe">

           Repository

        </a>

    </div>

</footer>
</body>
</html>
""")
