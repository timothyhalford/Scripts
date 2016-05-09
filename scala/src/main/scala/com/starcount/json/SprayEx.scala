import spray.json.DefaultJsonProtocol

object Utils {
  def main(args: Array[String]) {

    case class Token (network : String,
                      access_token : String,
                      name : String,
                      access_token_secret : String,
                      consumer_key : String,
                      consumer_secret : String,
                      is_valid : Boolean)

    object TokenProtocol extends DefaultJsonProtocol {
      implicit val tokenFormat = jsonFormat7(Token)
    }

    // You need to import your json converter protocol. This is the thing that is implied by convertTo
    import TokenProtocol._
    import spray.json._

    val token = Token("facebook", "token_1", "my_name", "accessToken", "consumer", "consum34", true)
    val singleTokenParsedAndConverted = single.parseJson.convertTo[Token]
    val listOfJsonTokensParsedAndConverted = source.parseJson.convertTo[List[Token]]
    val tokenObjectAsJson = token.toJson

    println(singleTokenParsedAndConverted)
    println(tokenObjectAsJson)
    println(listOfJsonTokensParsedAndConverted)
  }

  val source =
    """| [
      |  {
      |    "network": "twitter",
      |    "access_token": "130081980-DeingDke3hqT9oqeEq3LfPudhYs1yTl0hNZpM5ag",
      |    "name": "anggie nindya s",
      |    "access_token_secret": "1Ww2TmvKVdgLaQLJj2e4LCbhxMuNYvJhDbqLflW0M",
      |    "consumer_key": "9HXSwZSgqaUYNj2XinYBXw",
      |    "consumer_secret": "zdzbNfU1molP2m4w0AkksmIBmIUJCkhv1lU4",
      |    "is_valid": true
      |  },
      |  {
      |    "network": "twitter",
      |    "access_token": "1137525067-M8AuButn94ry2zx1jJKgZPFxswP209U55rVGpFg",
      |    "name": "sarah rios de abreu ",
      |    "access_token_secret": "tOJqSVPxePigBtTqkf6PLqMbrgFewXXBlE8yVojE",
      |    "consumer_key": "9HXSwZSgqaUYNj2XinYBXw",
      |    "consumer_secret": "zdzbNfU1molP2m4w0AkksmIBmIUJCkhv1lU4",
      |    "is_valid": true
      |  },
      |  {
      |    "network": "twitter",
      |    "access_token": "1336168296-hcy8ycIgtuCXjRVZlUkJbRGx4wo7yohiZGujHOb",
      |    "name": "concetta de paola",
      |    "access_token_secret": "wjd2I1FialV6m8QkjeUY7UVLrk58cAhSNlKUh2U2z9k",
      |    "consumer_key": "9HXSwZSgqaUYNj2XinYBXw",
      |    "consumer_secret": "zdzbNfU1molP2m4w0AkksmIBmIUJCkhv1lU4",
      |    "is_valid": true
      |  }
      |]"""
      .stripMargin

  val single =
    """
      |{
      |    "network": "twitter",
      |    "access_token": "130081980-DeingDke3hqT9oqeEq3LfPudhYs1yTl0hNZpM5ag",
      |    "name": "anggie nindya s",
      |    "access_token_secret": "1Ww2TmvKVdgLaQLJj2e4LCbhxMuNYvJhDbqLflW0M",
      |    "consumer_key": "9HXSwZSgqaUYNj2XinYBXw",
      |    "consumer_secret": "zdzbNfU1molP2m4w0AkksmIBmIUJCkhv1lU4",
      |    "is_valid": true
      |  }
    """.stripMargin
}
