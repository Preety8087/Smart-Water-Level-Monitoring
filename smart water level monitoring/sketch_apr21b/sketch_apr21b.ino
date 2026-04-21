const int trigPin = 9;
const int echoPin = 10;

const int LED1 = 2;
const int LED2 = 3;
const int LED3 = 4;
const int buzzer = 5;

long duration;
int distance;

void setup() {
  Serial.begin(9600);

  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);
  pinMode(buzzer, OUTPUT);
}

void loop() {

  // Trigger pulse
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // READ ECHO (with timeout to avoid 0 issue)
  duration = pulseIn(echoPin, HIGH, 30000);

  // If no signal
  if (duration == 0) {
    Serial.println(-1);   // debug value
    delay(500);
    return;
  }

  // Convert distance
  distance = duration * 0.034 / 2;

  // Send to Python
  Serial.println(distance);

  // LOGIC

  if (distance > 20) {
    digitalWrite(LED1, HIGH);
    digitalWrite(LED2, LOW);
    digitalWrite(LED3, LOW);
    digitalWrite(buzzer, LOW);
  }

  else if (distance > 10 && distance <= 20) {
    digitalWrite(LED1, LOW);
    digitalWrite(LED2, HIGH);
    digitalWrite(LED3, LOW);
    digitalWrite(buzzer, LOW);
  }

  else {
    digitalWrite(LED1, LOW);
    digitalWrite(LED2, LOW);
    digitalWrite(LED3, HIGH);
    digitalWrite(buzzer, HIGH);
  }

  delay(700);
}