from survey.settings import STATICFILES_DIRS
import os

from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, HRFlowable, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch

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

        # Header
        header = Paragraph('This is a multi-line header. It goes on every page. ' * 5, styles['Normal'])
        w, h = header.wrap(doc.width, doc.topMargin)
        header.drawOn(canvas, doc.leftMargin, doc.height + doc.topMargin - h)

        # Footer
        footer = Paragraph('This is a multi-line header. It goes on every page. ' * 5, styles['Normal'])
        w, h = footer.wrap(doc.width, doc.bottomMargin)
        footer.drawOn(canvas, doc.leftMargin, h)

        canvas.restoreState()


    def makePDF(self, data):
        try:
            buffer = self.buffer
            doc = SimpleDocTemplate(buffer, 
                                    rightMargin=inch/4,
                                    leftMargin=inch/4, 
                                    topMargin=inch,
                                    bottomMargin=inch/2, 
                                    pagesize=self.pagesize)
            elements = []
            styles = getSampleStyleSheet()
            styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))

            elements.append(Paragraph('My questions are', styles['Heading1']))

            for key, value in data.items():
                elements.append(Paragraph(str(key) + '. Question:', styles['Heading5']))
                elements.append(Paragraph(value[0], styles['Normal']))
                elements.append(Spacer(0, 7))
                elements.append(Paragraph('Your Answer:', styles['Heading5']))
                elements.append(Paragraph(value[1], styles['Normal']))
                elements.append(Spacer(0, 7))
                elements.append(Paragraph('Recommendation:', styles['Heading5']))
                elements.append(Paragraph(value[2], styles['Normal']))
                elements.append(Spacer(0, 5))
                elements.append(HRFlowable(width="100%", thickness=1, lineCap='round', spaceBefore=1, spaceAfter=1, hAlign='CENTER', vAlign='BOTTOM', dash=None))

            doc.build(elements, onFirstPage=self._header_footer, onLaterPages=self._header_footer)
        except:
            return False
        else:
            return True