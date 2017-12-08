import java.io.File;

import javax.xml.transform.Result;
import javax.xml.transform.Source;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerConfigurationException;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.stream.StreamResult;
import javax.xml.transform.stream.StreamSource;
public class ChangeXmlToHtml {

    public static void Transform(String xmlFileName, String xslFileName,
                                 String htmlFileName) {
        try {
            TransformerFactory tFac = TransformerFactory.newInstance();
            Source xslSource = new StreamSource(xslFileName);
            Transformer t = tFac.newTransformer(xslSource);
            File xmlFile = new File(xmlFileName);
            File htmlFile = new File(htmlFileName);
            Source source = new StreamSource(xmlFile);
            Result result = new StreamResult(htmlFile);
            System.out.println(result.toString());
            t.transform(source, result);
        } catch (TransformerConfigurationException e) {
            e.printStackTrace();
        } catch (TransformerException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) throws Exception {
        // TODO Auto-generated method stub
        //String xmlFileName = "/Users/liufm/Desktop/findbugs.xml";
        String xmlFileName = args[0];
        System.out.print（"传入xml文件成功"）
        //String xslFileName = "/Users/liufm/Desktop/fancy-hist.xsl";
        String xslFileName = args[1];
        //String htmlFileName = "/Users/liufm/Desktop/fancy-histxml.html";
        String htmlFileName = args[2];
        Transform(xmlFileName, xslFileName, htmlFileName);
        System.out.print("输出html文档成功！");
    }

}
