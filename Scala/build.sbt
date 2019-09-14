lazy val root = project
  .in(file("."))
  .enablePlugins(ScalaJSPlugin)
  .settings(
    inThisBuild(List(
      organization := "com.ggzor",
      version      := "0.1",
      scalaVersion := "2.13.0"
    )),
    name := "quin-mccluskey",
    libraryDependencies ++= Seq(
      "org.scalatest" %%% "scalatest"      % "3.0.8"    % "test"
    ),
    scalaJSUseMainModuleInitializer := true
  )
