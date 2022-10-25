//
//  Landmark.swift
//  Lunch Lottery
//
//  Created by TommyVC04 on 8/31/22.
//

import SwiftUI
import Foundation
import CoreLocation

struct Landmark: Hashable, Codable, Identifiable {
    var id: Int
    var time: Int
    var name: String
    var park: String
    var state: String
    var description: String
    var isFeatured: Bool
    var isConfirmed: Bool
    
    var category: Category
    enum Category: String, CaseIterable, Codable {
        case test = "Test"
        case lfhs = "Lake Forest High School"
        case dpm = "Deerpath Middle School"
        case lbes = "Lake Bluff Elementary School"
    }
    
    var timeStr: String {
        let first = String(time/100)
        let second = String(time%100)
        return first + ":" + second
    }

    private var imageName: String
    var image: Image {
        Image(imageName)
    }

    var featureImage: Image? {
        isFeatured ? Image(imageName + "_feature") : nil
    }
}
