name := "SparkExamples"
version := "0.0.0"
scalaVersion := "2.10.0"

fullResolvers += "jcenter" at "https://jcenter.bintray.com/"

libraryDependencies ++= Seq(
  ("org.apache.spark" % "spark-core_2.10" % "1.5.2")
    .exclude("org.scala-lang", "scala-library")
    .exclude("org.scala-lang", "scala-reflect")
    .exclude("org.apache.commons", "commons-lang3")
    .exclude("org.slf4j", "slf4j-api"),
  ("org.apache.spark" % "spark-sql_2.10" % "1.5.2")
    .exclude("org.scala-lang", "scala-library")
    .exclude("org.scala-lang", "scala-reflect"),
  "com.databricks" %% "spark-avro" % "2.0.1",
  "io.spray" %%  "spray-json" % "1.3.2",
  "org.scalatest" % "scalatest_2.10" % "2.0" % "test"
)

assemblyMergeStrategy in assembly := {
  case x if x.startsWith("META-INF") => MergeStrategy.discard
  case _ => MergeStrategy.first
}

mainClass in assembly := Some("com.starcount.spark.examples.AvroToParquet")
test in assembly := {}

