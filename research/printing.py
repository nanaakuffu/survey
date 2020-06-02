from survey.settings import STATICFILES_DIRS

from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, HRFlowable, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from reportlab.lib.units import inch, mm
from reportlab.lib import colors

class PDF():
    def __init__(self, buffer, pagesize):
        self.buffer = buffer
        if pagesize == 'A4':
            self.pagesize = A4
        elif pagesize == 'Letter':
            self.pagesize = letter
        
        self.width, self.height = self.pagesize

    @staticmethod
    def _header_footer(canvas, doc):
        canvas.saveState()
        styles = getSampleStyleSheet()

        customColor = colors.Color(red=(46/255),green=(117/255),blue=(181/255))

        style_right = ParagraphStyle(name='right',
                                     alignment=TA_RIGHT,
                                     textColor=customColor)
        style_center = ParagraphStyle(name='center',
                                     alignment=TA_CENTER,
                                     textColor=colors.black)
        
        # Header
        IMAGE_PATH = STATICFILES_DIRS[0] + "/survey/img/new_survey_logo.jpg"
        imageHeader = Image(IMAGE_PATH, 4.1 * inch, 1.2 * inch)
        imageHeader.hAlign = 'LEFT'
        headerText = Paragraph('<font size="20"><b>MyBQualityScan</b></font>', style_right)
        subheaderText = Paragraph('<font size="15"><b>QI Recommendation</b></font>', style_right)

        # This is needed for the drawOn for Paragraph to work
        w, h = headerText.wrap(doc.width, doc.topMargin)
        w1, h1 = subheaderText.wrap(doc.width, doc.topMargin)
        # Draw image and Text on the pdf canvas
        imageHeader.drawOn(canvas, doc.leftMargin, doc.height + doc.topMargin - 30)
        headerText.drawOn(canvas, doc.leftMargin - 10, doc.height + doc.topMargin + 30)
        subheaderText.drawOn(canvas, doc.leftMargin - 10, doc.height + doc.topMargin)

        # Footer
        page_number_text = "%d" % (doc.page)
        footer = Paragraph(page_number_text, style_center)
        w, h = footer.wrap(doc.width, doc.bottomMargin)
        footer.drawOn(canvas, doc.leftMargin, h + 20)

        canvas.restoreState()


    def makePDF(self, hData, data):
        try:
            buffer = self.buffer
            pdfDocument = SimpleDocTemplate(buffer, 
                                    rightMargin=inch/3,
                                    leftMargin=inch/3, 
                                    topMargin=inch * 1.5,
                                    bottomMargin=inch * 1, 
                                    pagesize=self.pagesize)
            pdfElements = []
            styles = getSampleStyleSheet()
            styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))

            space = ' &nbsp;' * 17

            headerText = "<b>Name: </b> %s %s <b>Facility Name: </b> %s" % (hData['name'], space, hData['facility'])
            pdfElements.append(Paragraph(headerText, styles['Normal']))
            pdfElements.append(Spacer(0, 3))
            dateText = "<b>Survey Date:</b> %s" % hData['date']
            pdfElements.append(Paragraph(dateText, styles['Normal']))
            pdfElements.append(Spacer(0, 5))
            # Draw a line under the headers
            pdfElements.append(HRFlowable(width="100%", color=colors.black))

            for key, value in data.items():
                pdfElements.append(Spacer(0, 5))
                pdfElements.append(Paragraph('<b>' + str(key) + '. Question:</b>', styles['Normal']))
                pdfElements.append(Paragraph(value[0], styles['Normal']))
                pdfElements.append(Spacer(0, 5))
                pdfElements.append(Paragraph('<b>Your Answer:</b>', styles['Normal']))
                pdfElements.append(Paragraph(value[1], styles['Normal']))
                pdfElements.append(Spacer(0, 5))
                pdfElements.append(Paragraph('<b>Recommendation:</b>', styles['Normal']))
                pdfElements.append(Paragraph(value[2], styles['Normal']))
                pdfElements.append(Spacer(0, 5))
                pdfElements.append(HRFlowable(width="100%", color=colors.black))

            pdfDocument.build(pdfElements, 
                            onFirstPage=self._header_footer, 
                            onLaterPages=self._header_footer)
        except:
            return False
        else:
            return True