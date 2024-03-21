#define S0_PIN PB5 
#define S1_PIN PB6
#define S2_PIN PB9
#define S3_PIN PB8
#define OUT_PIN  PB7

#define RED_THRESHOLD 80   //64
#define GREEN_THRESHOLD 80  //63
#define PINK_THRESHOLD 32 
#define BLUE_THRESHOLD 80  


int process_red_value();
int process_green_value();
int process_blue_value();

void setup() {
  // Set the S0, S1, S2, S3 Pins as Output
  pinMode(S0_PIN, OUTPUT);
  pinMode(S1_PIN, OUTPUT);
  pinMode(S2_PIN, OUTPUT);
  pinMode(S3_PIN, OUTPUT);
 //Set OUT_PIN as Input
  pinMode(OUT_PIN, INPUT);
 // Set Pulse Width scaling to 20%
  digitalWrite(S0_PIN, HIGH);
  digitalWrite(S1_PIN, LOW);
 // Enable UART for Debugging
  Serial.begin(9600);

}

void loop() {
  int r, g, b;
  r = process_red_value();
  delay(200);
  g = process_green_value();
  delay(200);
  b = process_blue_value();
  delay(200);
  Serial.print("r = ");
  Serial.print(r);
  Serial.print(" ");
  Serial.print("g = ");
  Serial.print(g);
  Serial.print(" ");
  Serial.print("b = ");
  Serial.print(b);
  Serial.print(" ");
  Serial.println();
  if (r < PINK_THRESHOLD)
  {
    Serial.println("Colour Pink");
  }
  else if (g < GREEN_THRESHOLD)
  {
    Serial.println("Colour Green");
  }
  else if (r < RED_THRESHOLD)
  {
    Serial.println("Colour Red");
  }
  else if (b < BLUE_THRESHOLD)
  {
    Serial.println("Colour Blue");    
  }

}

int process_red_value()
{
  digitalWrite(S2_PIN, LOW);
  digitalWrite(S3_PIN, LOW);
  int pulse_length = pulseIn(OUT_PIN, LOW);
  return pulse_length;
}
int process_green_value()
{
  digitalWrite(S2_PIN, HIGH);
  digitalWrite(S3_PIN, HIGH);
  int pulse_length = pulseIn(OUT_PIN, LOW);
  return pulse_length;
}
int process_blue_value()
{
  digitalWrite(S2_PIN, LOW);
  digitalWrite(S3_PIN, HIGH);
  int pulse_length = pulseIn(OUT_PIN, LOW);
  return pulse_length;
}
