//
//  testApp.swift
//  test
//
//  Created by Станислав Билим on 28.02.2023.
//

import SwiftUI

@main
struct testApp: App {
    var body: some Scene {
        DocumentGroup(newDocument: testDocument()) { file in
            ContentView(document: file.$document)
        }
    }
}
