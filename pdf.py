from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from banco import listar_pessoas


def gerar_pdf():
    # Nome do arquivo PDF
    caminho = "pessoas_cadastradas.pdf"

    # Cria o documento em modo paisagem
    documento = SimpleDocTemplate(
        caminho,
        pagesize=landscape(A4),
        rightMargin=8 * mm,
        leftMargin=8 * mm,
        topMargin=8 * mm,
        bottomMargin=8 * mm
    )

    # Busca as pessoas no banco
    pessoas = listar_pessoas()

    # Cabeçalho da tabela
    dados = [[
        "ID", "Nome", "Tipo", "Documento", "E-mail",
        "Celular", "CEP", "Logradouro", "Número",
        "Complemento", "Bairro", "Cidade", "Estado"
    ]]

    # Adiciona os cadastros
    for pessoa in pessoas:
        dados.append([
            str(valor or "")
            for valor in pessoa
        ])

    # Cria a tabela
    tabela = Table(dados, repeatRows=1)

    # Estilo da tabela
    tabela.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 6),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [
            colors.white,
            colors.whitesmoke
        ]),
    ]))

    # Monta e salva o PDF
    documento.build([tabela])

    return caminho