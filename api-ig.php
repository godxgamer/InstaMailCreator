<?php

// Set your proxy and number here
$proxy = "enter your proxy here"; // "username:password@host:port" (without http:// or https:// )
$number = "enter your number here"; // example "919988776655" (without + )

// Define the JSON data payload
$data = array(
    "api-key" => "gamer",
    "number" => $number,
    "proxy" => $proxy
);

$headers = array(
    "Content-Type: application/json"
);

// Make the first POST request
$ch = curl_init("http://128.140.99.16:6969/api/send-sms");
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_TIMEOUT, 100);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($ch);
$http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

// Check if "securetoken" is in the response
if (strpos($response, "securetoken") !== false) {
    echo $response . "\n";
    $response_data = json_decode($response, true);
    $securetoken = $response_data['message']['securetoken'];
    echo "otp : ";
    $otp = trim(fgets(STDIN));

    // Define the JSON data payload for the second POST request
    $data = array(
        "api-key" => "gamer",
        "securetoken" => $securetoken,
        "proxy" => $proxy,
        "otp" => $otp
    );

    // Make the second POST request
    $ch = curl_init("http://128.140.99.16:6969/api/create-acc");
    curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_TIMEOUT, 100);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    $response = curl_exec($ch);
    echo $response . "\n";
    curl_close($ch);
} else {
    echo $response . "\n";
}
?>
