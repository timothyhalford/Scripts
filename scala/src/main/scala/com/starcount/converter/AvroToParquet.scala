import scala.io.Source

object AvroToParquet {

  def getListOfFiles(directory_uri: String): List[file] = {
    val directory = File(directory_uri)
    if(directory.exists && directory.isDirectory) {
      directory.listFiles.filter(_.isFile).toList
    } else {
      List[File]()
    }
  }

  def writeFile

  def main(args: Array[String]): Unit = {
    

  }
}
