#include "test1.h"
#include "ui_test1.h"

void test1::db_open_database(){
    db = QSqlDatabase::addDatabase("QMYSQL");
    db.setHostName("localhost");
    db.setUserName("root");
    db.setPassword("");
    db.setDatabaseName(dbase);

    if (!db.open()) {
        QMessageBox::critical(this,"Error","Error Opening Database");
        return;
    }
}

void test1::db_export_pdf(){
    QString fileName = QFileDialog::getSaveFileName((QWidget* )0, "Export PDF", QString(), "*.pdf");
    if(fileName.isEmpty()){return;}
    if (QFileInfo(fileName).suffix().isEmpty()) { fileName.append(".pdf"); }

    QPrinter printer(QPrinter::PrinterResolution);
    printer.setOutputFormat(QPrinter::PdfFormat);
    printer.setPaperSize(QPrinter::A4);
    printer.setOutputFileName(fileName);

    QTextDocument doc;
    doc.setHtml("<h1>Hello, World!</h1>\n<p>Lorem ipsum dolor sit amet, consectitur adipisci elit.</p>");
    doc.setPlainText("Coba \n PDF");
    doc.setPageSize(printer.pageRect().size()); // This is necessary if you want to hide the page number
    doc.print(&printer);
}
