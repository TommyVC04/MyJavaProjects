//
//  Profile.swift
//  Lunch Lottery
//
//  Created by TommyVC04 on 9/14/22.
//

import Foundation

struct Profile {
    var username: String
    var prefersNotifications = true
    var school = School.none
    var goalDate = Date()

    static let `default` = Profile(username: "")

    enum School: String, CaseIterable, Identifiable {
        case none = "Choose a School / Organization"
        case lakeForestHighSchool = "Lake Forest High School"
        case deerpathMiddleSchool = "Deerpath Middle School"
        case lakeBluffElementary = "Lake Bluff Elementary School"

        var id: String { rawValue }
    }
}
