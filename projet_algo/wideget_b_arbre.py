from PyQt6.QtWidgets import QWidget, QScrollArea, QLabel,QVBoxLayout,QFrame,QPushButton,QFileDialog
from PyQt6.QtGui import QPixmap,QMovie
from PyQt6.QtCore import Qt
import shutil
import os
from home_pages import home_pages
class learn_b_arbre(QWidget):
    def __init__(self):
        super().__init__()

        # Scroll Area
        scroll_area = QScrollArea()
        scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground,True)
        scroll_area.setStyleSheet("""
            QScrollArea {
                border: none;
                background:transparent;
            }
            QScrollBar:vertical {
                background-color: #f0f0f0;
                width: 12px;
                border-radius: 6px;
            }
            QScrollBar::handle:vertical {
                background-color: #606060;
                border-radius: 6px;
                min-height: 20px;
            }
            QScrollBar::handle:vertical:hover {
                background-color: #404040;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                background: none;
            }
            QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
                background: none;
            }
            QScrollBar:horizontal {
                background-color: #f0f0f0;
                height: 12px;
                border-radius: 6px;
            }
            QScrollBar::handle:horizontal {
                background-color: #606060;
                border-radius: 6px;
                min-width: 20px;
            }
            QScrollBar::handle:horizontal:hover {
                background-color: #404040;
            }
            QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
                background: none;
            }
            QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {
                background: none;
            }
        """)
        scroll_area.setWidgetResizable(True)
        content_widget = QWidget(self)
        content_widget.setStyleSheet("background:transparent;")
        label_definition_titre = QLabel("1.Explication Algorithme B_arbre", content_widget)
        label_definition_titre.setStyleSheet("color:red;font-size:16px")
        label_definition_titre.setGeometry(10, 0, 230, 30)  #
        #
        #pour telecharge les cours 
        self.label_description_telcharge=QLabel("clic ici pour telcharge le cours de B_arbre de Prof OQAIDI",content_widget)
        self.label_description_telcharge.setGeometry(272,30,310,17)
        self.label_description_telcharge.setStyleSheet("font-family:'robot';")
        self.nvtelcharge=QLabel(content_widget)
        self.nvtelcharge.setGeometry(270,50,550,90)
        self.nvtelcharge.setStyleSheet("background:#b1b3b6;border:solid white 2px; border-radius:15px;")
        self.icone_telecharge=QPixmap("projet/install.png")
        self.label_icon_telecharge=QLabel(content_widget)
        self.label_icon_telecharge.setPixmap(self.icone_telecharge)
        self.label_icon_telecharge.setGeometry(278,74,45,45)
        self.label_icon_telecharge.setScaledContents(True)
        self.tap_here_to_install=QLabel("Tap here to install",content_widget)
        self.tap_here_to_install.setGeometry(330,70,100,20)
        self.tap_here_to_install.setStyleSheet("color:black;font-weight:600;")
        self.nom_ficihier=QLabel("Séance_5_Algo-avancée.pdf",content_widget)
        self.nom_ficihier.setGeometry(330,90,220,30)
        self.nom_ficihier.setStyleSheet("color:white;")
        self.telcharge_cours=QPushButton("Save As",content_widget)
        self.telcharge_cours.setStyleSheet("background:white;color:black;font-family:'Roboto';border:solid black 5px; border-radius:10px; border-color:black;font-size:14px;")
        self.telcharge_cours.setGeometry(745,80,60,30)
        self.telcharge_cours.clicked.connect(self.telchargefile)
        # Definition text
        
        label_definition = QLabel(
            "Un B-arbre est une structure de données d'arbre équilibré utilisée principalement dans les systèmes de bases\nde données et les systèmes de\nfichiers pour organiser et stocker de grandes quantités\nde données sur disque ou autres périphériques de stockage.\nLe B-arbre garantit que les opérations de recherche,\ninsertion et suppression s'exécutent de manière efficace,\nmême lorsque les données ne tiennent pas en mémoire principale", content_widget
        )
        label_definition.setStyleSheet("color:black;font-size:12px;")
        label_definition.setGeometry(10, 170, 570, 110)  
        
        images_definition_dijikstre = QMovie("projet/b_arbregif.gif")
        label_images_definiton = QLabel(content_widget)
        label_images_definiton.setMovie(images_definition_dijikstre)
        label_images_definiton.setGeometry(600, 140, 400, 400)
        label_images_definiton.setScaledContents(True)
        images_definition_dijikstre.start()
       
        #Fonctionnement de l'algorithme de Dijkstra
        self.label_foncationement=QLabel("2.Avantages du B-arbre :",content_widget)
        self.label_foncationement.setGeometry(10,280,350,30)
        self.label_foncationement.setStyleSheet("color:red;font-size:15px")
        scroll_area.setWidget(content_widget)
        
        #Initialisation 
        self.Initialisationlabel=QLabel("2.1Efficacité sur disque",content_widget)
        self.Initialisationlabel.setGeometry(15,300,350,30)
        self.Initialisationlabel.setStyleSheet("color:green;font-size:15px")
        self.label_initeil_desc=QLabel("1.Conçu pour minimiser les opérations d'entrée/sortie (I/O) en regroupant plusieurs \nclés dans un seul nœud",content_widget)
        self.label_initeil_desc.setGeometry(18,310,460,60)
        #Étape principale
        self.principale=QLabel("2.2 Équilibre garanti",content_widget)
        self.principale.setGeometry(15,360,370,30)
        self.principale.setStyleSheet("color:green;font-size:15px")
        self.principale_desc=QLabel("1.L'arbre reste équilibré, maintenant les opérations\n(recherche, insertion, suppression) efficaces.",content_widget)
        self.principale_desc.setGeometry(18,370,460,60)
        #etape marquage
        self.Marquage_title=QLabel("2.3Utilisation optimale de l'espace",content_widget)
        self.Marquage_title.setGeometry(15,420,290,30)
        self.Marquage_title.setStyleSheet("color:green;font-size:15px;")
        self.Marquage_description1=QLabel("Les clés sont réparties uniformément entre les nœuds.",content_widget)
        self.Marquage_description1.setGeometry(18,440,300,35)
        
        content_widget.setFixedSize(1000, 750)
        scroll_area.setWidget(content_widget)
        #-------------------------------
        
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)
    def telchargefile(self):
        file_dialoge=QFileDialog(self)
        file_dialoge.setFileMode(QFileDialog.FileMode.Directory)
        file_dialoge.setOption(QFileDialog.Option.ShowDirsOnly, True)
        folder = file_dialoge.getExistingDirectory(self, "Sélectionner un dossier de destination")
        if folder:
            src_file = "fichier_a_telcharge/Séance_4_Algo-avancée.pdf"
            dest_file = os.path.join(folder, "Séance_4_Algo-avancée.pdf")
            
            try:
                shutil.copy(src_file, dest_file)
                print(f"Le fichier a été téléchargé vers: {dest_file}")
            except Exception as e:
                print(f"Erreur lors du téléchargement du fichier: {e}")

