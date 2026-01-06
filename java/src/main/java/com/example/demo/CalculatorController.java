package com.example.demo;

import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

@RestController
public class CalculatorController {

    @GetMapping(value = "calc")
    public String calculator(
            @RequestParam int a,
            @RequestParam int b,
            @RequestParam String op
    ) {

        switch (op) {
            case "add":
                return "Result = " + (a + b);

            case "sub":
                return "Result = " + (a - b);

            case "mul":
                return "Result = " + (a * b);

            case "div":
                if (b == 0) {
                    return "Error: Division by zero";
                }
                return "Result = " + (a / b);

            default:
                return "Invalid operation. Use add, sub, mul, or div";
        }
    }
}
