from mybqualityscan.settings import STATICFILES_DIRS

from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, HRFlowable, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from reportlab.lib.units import inch, mm
from reportlab.lib import colors


class PDF:
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

        custom_color = colors.Color(
            red=(46 / 255), green=(117 / 255), blue=(181 / 255))

        style_right = ParagraphStyle(name='right',
                                     alignment=TA_RIGHT,
                                     textColor=custom_color)
        style_center = ParagraphStyle(name='center',
                                      alignment=TA_CENTER,
                                      textColor=colors.black)

        # Header
        image_path = STATICFILES_DIRS[0] + "/survey/img/new_survey_logo.jpg"
        image_header = Image(image_path, 4.1 * inch, 1.2 * inch)
        image_header.hAlign = 'LEFT'
        header_text = Paragraph(
            '<font size="20"><b>MyBQualityScan</b></font>', style_right)
        subheader_text = Paragraph(
            '<font size="15"><b>QI Recommendation</b></font>', style_right)

        # This is needed for the drawOn for Paragraph to work
        w, h = header_text.wrap(doc.width, doc.topMargin)
        w1, h1 = subheader_text.wrap(doc.width, doc.topMargin)
        # Draw image and Text on the pdf canvas
        image_header.drawOn(canvas, doc.leftMargin,
                            doc.height + doc.topMargin - 30)
        header_text.drawOn(canvas, doc.leftMargin - 10,
                           doc.height + doc.topMargin + 30)
        subheader_text.drawOn(canvas, doc.leftMargin - 10,
                              doc.height + doc.topMargin)

        # Footer
        page_number_text = "%d" % (doc.page)
        footer = Paragraph(page_number_text, style_center)
        w, h = footer.wrap(doc.width, doc.bottomMargin)
        footer.drawOn(canvas, doc.leftMargin, h + 20)

        canvas.restoreState()

    def make_pdf(self, header_data, data):
        try:
            buffer = self.buffer
            pdf_document = SimpleDocTemplate(buffer,
                                             rightMargin=inch / 3,
                                             leftMargin=inch / 3,
                                             topMargin=inch * 1.5,
                                             bottomMargin=inch * 1,
                                             pagesize=self.pagesize)
            pdf_elements = []
            styles = getSampleStyleSheet()
            styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))

            space = ' &nbsp;' * 17

            header_text = "<b>Name: </b> %s %s <b>Facility Name: </b> %s" % (
                header_data['name'],
                space,
                header_data['facility'])

            pdf_elements.append(Paragraph(header_text, styles['Normal']))
            pdf_elements.append(Spacer(0, 3))
            date_text = "<b>Survey Date:</b> %s" % header_data['date']
            pdf_elements.append(Paragraph(date_text, styles['Normal']))
            pdf_elements.append(Spacer(0, 5))
            # Draw a line under the headers
            pdf_elements.append(HRFlowable(width="100%", color=colors.black))

            for key, value in data.items():
                pdf_elements.append(Spacer(0, 5))
                pdf_elements.append(
                    Paragraph('<b>' + str(key) + '. Question:</b>', styles['Normal']))
                pdf_elements.append(Paragraph(value[0], styles['Normal']))
                pdf_elements.append(Spacer(0, 5))
                pdf_elements.append(
                    Paragraph('<b>Your Answer:</b>', styles['Normal']))
                pdf_elements.append(Paragraph(value[1], styles['Normal']))
                pdf_elements.append(Spacer(0, 5))
                pdf_elements.append(
                    Paragraph('<b>Recommendation:</b>', styles['Normal']))
                pdf_elements.append(Paragraph(value[2], styles['Normal']))
                pdf_elements.append(Spacer(0, 5))
                pdf_elements.append(HRFlowable(
                    width="100%", color=colors.black))

            pdf_document.build(pdf_elements,
                               onFirstPage=self._header_footer,
                               onLaterPages=self._header_footer)
        except:
            return False
        else:
            return True
